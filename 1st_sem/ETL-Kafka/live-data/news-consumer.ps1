# ==============================================================================
# Kafka News Consumer (Compact Terminal Stream)
# ==============================================================================

$KafkaContainer = "kafka"
$KafkaTopic     = "global-news"

$Host.UI.RawUI.WindowTitle = "Kafka Consumer Feed"

Clear-Host
Write-Host "=== KAFKA CONSUMER STREAM: '$KafkaTopic' (localhost:9092) ===" -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop." -ForegroundColor DarkGray
Write-Host ""

$cmd = "docker exec -i $KafkaContainer /opt/kafka/bin/kafka-console-consumer.sh --topic $KafkaTopic --from-beginning --bootstrap-server localhost:9092 2>`$null"

$articleCount = 0

& powershell.exe -Command $cmd | ForEach-Object {
    $rawLine = $_.Trim()
    if (-not $rawLine) { return }

    try {
        $article = $rawLine | ConvertFrom-Json
        $articleCount++

        $publisher = if ($article.publisher) { $article.publisher } else { "Unknown" }
        $title     = if ($article.title.Length -gt 75) { $article.title.Substring(0, 72) + "..." } else { $article.title }
        $pubTime   = if ($article.published_at) { $article.published_at.Substring(11, 8) } else { "NOW" }

        Write-Host "[#$articleCount $pubTime] " -NoNewline -ForegroundColor DarkCyan
        Write-Host "$publisher " -NoNewline -ForegroundColor Yellow
        Write-Host "| " -NoNewline -ForegroundColor DarkGray
        Write-Host "$title" -ForegroundColor White
    }
    catch {
        Write-Host "[RAW] $rawLine" -ForegroundColor DarkGray
    }
}
