# ==========================================
# FreeNewsApi -> Apache Kafka Producer
# ==========================================

$KafkaContainer = "kafka"
$KafkaTopic = "global-news"

# API key is stored safely as a Windows environment variable
$ApiKey = $env:news_api

if (-not $ApiKey) {
    Write-Host "ERROR: news_api environment variable not found."
    exit
}

$headers = @{
    "x-api-key" = $ApiKey
}

$url = "https://api.freenewsapi.io/v1/news?language=en&topic=world&order_by=recent"

# Remember articles already sent during this session
$SeenArticles = @{}

Write-Host ""
Write-Host "======================================="
Write-Host "   LIVE GLOBAL NEWS -> APACHE KAFKA"
Write-Host "======================================="
Write-Host ""
Write-Host "Kafka topic : $KafkaTopic"
Write-Host "Refresh     : 60 seconds"
Write-Host ""
Write-Host "Press Ctrl+C to stop."
Write-Host ""

while ($true) {

    try {

        Write-Host "Fetching latest world news..."

        $response = Invoke-RestMethod `
            -Uri $url `
            -Headers $headers `
            -Method Get

        foreach ($article in $response.data) {

            # Prefer UUID for deduplication
            $id = $article.uuid

            if (-not $id) {
                $id = $article.url
            }

            if ($SeenArticles.ContainsKey($id)) {
                continue
            }

            $SeenArticles[$id] = $true

            $message = @{
                uuid         = $article.uuid
                title        = $article.title
                publisher    = $article.publisher
                published_at = $article.published_at
                url          = $article.url
            }

            $json = $message | ConvertTo-Json -Compress

            # Send JSON to Kafka
            $json |
                docker exec -i $KafkaContainer `
                /opt/kafka/bin/kafka-console-producer.sh `
                --topic $KafkaTopic `
                --bootstrap-server localhost:9092

            Write-Host ""
            Write-Host "Published:"
            Write-Host $article.title
            Write-Host "Publisher: $($article.publisher)"
        }

        Write-Host ""
        Write-Host "Waiting 60 seconds..."
        Write-Host ""

    }
    catch {

        Write-Host ""
        Write-Host "ERROR:"
        Write-Host $_.Exception.Message
        Write-Host ""
        Write-Host "Retrying in 60 seconds..."
    }

    Start-Sleep -Seconds 60
}