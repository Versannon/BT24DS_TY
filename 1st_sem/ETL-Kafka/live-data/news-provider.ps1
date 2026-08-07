# ==============================================================================
# Kafka News Producer (Compact Terminal Feed)
# ==============================================================================

$KafkaContainer = "kafka"
$KafkaTopic     = "global-news"
$ApiKey         = $env:news_api

if (-not $ApiKey) {
    Write-Host "ERROR: 'news_api' environment variable not set." -ForegroundColor Red
    exit 1
}

$headers = @{ "x-api-key" = $ApiKey }
$url     = "https://api.freenewsapi.io/v1/news?language=en&topic=world&order_by=recent"

$SeenArticles  = @{}
$TotalSent     = 0

Clear-Host
Write-Host "=== KAFKA PRODUCER: FreeNewsAPI -> '$KafkaTopic' (60s loop) ===" -ForegroundColor Cyan
Write-Host ""

while ($true) {
    try {
        $timestamp = (Get-Date).ToString("HH:mm:ss")
        $response  = Invoke-RestMethod -Uri $url -Headers $headers -Method Get
        $newCount  = 0

        foreach ($article in $response.data) {
            $id = $article.uuid
            if (-not $id) { $id = $article.url }
            if (-not $id -or $SeenArticles.ContainsKey($id)) { continue }

            $SeenArticles[$id] = $true
            $TotalSent++
            $newCount++

            $message = @{
                uuid         = $article.uuid
                title        = $article.title
                publisher    = $article.publisher
                published_at = $article.published_at
                url          = $article.url
            }

            $json = $message | ConvertTo-Json -Compress
            $json | docker exec -i $KafkaContainer /opt/kafka/bin/kafka-console-producer.sh --topic $KafkaTopic --bootstrap-server localhost:9092 2>$null

            $publisher = if ($article.publisher) { $article.publisher } else { "Unknown" }
            $title     = if ($article.title.Length -gt 75) { $article.title.Substring(0, 72) + "..." } else { $article.title }

            Write-Host "[$timestamp] " -NoNewline -ForegroundColor DarkGray
            Write-Host "[PUB #$TotalSent] " -NoNewline -ForegroundColor Green
            Write-Host "$title " -NoNewline -ForegroundColor White
            Write-Host "($publisher)" -ForegroundColor Yellow
        }

        if ($newCount -eq 0) {
            Write-Host "[$timestamp] [IDLE] No new articles (Session Total: $TotalSent)" -ForegroundColor DarkGray
        }
    }
    catch {
        Write-Host "[$((Get-Date).ToString("HH:mm:ss"))] [ERROR] $($_.Exception.Message)" -ForegroundColor Red
    }

    Start-Sleep -Seconds 60
}