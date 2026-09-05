# ==============================================================================
# Open-Meteo Weather Terminal Provider (PowerShell CLI Contingency)
# Location: New Delhi (28.6139° N, 77.209° E)
# ==============================================================================

[CmdletBinding()]
param(
    [string]$ApiUrl = "https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.209&daily=rain_sum&hourly=temperature_2m,wind_speed_10m,relative_humidity_2m,apparent_temperature,rain,surface_pressure&timezone=auto",
    [switch]$Watch
)

$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

function Show-Weather {
    $now = Get-Date
    $timeStr = $now.ToString("yyyy-MM-dd HH:mm:ss")
    
    try {
        $response = Invoke-RestMethod -Uri $ApiUrl -Method Get -TimeoutSec 10
    }
    catch {
        Write-Host "[$timeStr] ERROR: Failed to fetch weather data from API." -ForegroundColor Red
        Write-Host "Details: $($_.Exception.Message)" -ForegroundColor DarkRed
        return
    }

    Clear-Host
    Write-Host ("=" * 85) -ForegroundColor Cyan
    Write-Host " [METEO LIVE] OPEN-METEO WEATHER TERMINAL REPORT" -ForegroundColor White
    Write-Host " Location : New Delhi (Lat: $($response.latitude) N, Lon: $($response.longitude) E) | Timezone: $($response.timezone)" -ForegroundColor Gray
    Write-Host " Timestamp: $timeStr | Elevation: $($response.elevation) m" -ForegroundColor Gray
    Write-Host ("=" * 85) -ForegroundColor Cyan
    Write-Host ""

    # Determine current hourly index
    $hourlyTimes = $response.hourly.time
    $currentIso = $now.ToString("yyyy-MM-ddTHH:00")
    
    $idx = [array]::IndexOf($hourlyTimes, $currentIso)
    if ($idx -lt 0) { $idx = 0 } # fallback if exact hour not matched

    $temp        = $response.hourly.temperature_2m[$idx]
    $feels       = $response.hourly.apparent_temperature[$idx]
    $humidity    = $response.hourly.relative_humidity_2m[$idx]
    $wind        = $response.hourly.wind_speed_10m[$idx]
    $rain        = $response.hourly.rain[$idx]
    $pressure    = $response.hourly.surface_pressure[$idx]
    $todayRain   = $response.daily.rain_sum[0]

    # Current Metrics Box
    Write-Host "+-----------------------------------------------------------------------------------+" -ForegroundColor Yellow
    Write-Host "| REAL-TIME WEATHER SNAPSHOT                                                        |" -ForegroundColor Yellow
    Write-Host "+-----------------------------------------------------------------------------------+" -ForegroundColor Yellow

    Write-Host "| Temperature        : " -NoNewline -ForegroundColor Gray
    Write-Host ("{0,-10}" -f "$temp C") -NoNewline -ForegroundColor Green
    Write-Host "| Feels Like     : " -NoNewline -ForegroundColor Gray
    Write-Host ("{0,-15}" -f "$feels C") -ForegroundColor DarkGreen

    Write-Host "| Relative Humidity  : " -NoNewline -ForegroundColor Gray
    Write-Host ("{0,-10}" -f "$humidity %") -NoNewline -ForegroundColor Cyan
    Write-Host "| Wind Speed     : " -NoNewline -ForegroundColor Gray
    Write-Host ("{0,-15}" -f "$wind km/h") -ForegroundColor Blue

    Write-Host "| Surface Pressure   : " -NoNewline -ForegroundColor Gray
    Write-Host ("{0,-10}" -f "$pressure hPa") -NoNewline -ForegroundColor Yellow
    Write-Host "| Current Rain   : " -NoNewline -ForegroundColor Gray
    if ($rain -gt 0) {
        Write-Host ("{0,-15}" -f "$rain mm (Raining)") -ForegroundColor Magenta
    } else {
        Write-Host ("{0,-15}" -f "$rain mm (Dry)") -ForegroundColor DarkGray
    }

    Write-Host "| Today Rain Total   : " -NoNewline -ForegroundColor Gray
    Write-Host ("{0,-42}" -f "$todayRain mm") -ForegroundColor DarkCyan
    Write-Host "+-----------------------------------------------------------------------------------+" -ForegroundColor Yellow
    Write-Host ""

    # Next 12 Hours Forecast Table
    Write-Host "NEXT 12 HOURS FORECAST:" -ForegroundColor Yellow
    Write-Host ("{0,-18} | {1,-10} | {2,-12} | {3,-10} | {4,-10} | {5,-12}" -f "Time (ISO)", "Temp (C)", "Feels (C)", "Rain (mm)", "Wind(km/h)", "Pressure(hPa)") -ForegroundColor DarkYellow
    Write-Host ("-" * 85) -ForegroundColor DarkGray

    $endIdx = [Math]::Min($idx + 12, $hourlyTimes.Count - 1)
    for ($i = $idx; $i -lt $endIdx; $i++) {
        $t = $hourlyTimes[$i]
        $tmp = $response.hourly.temperature_2m[$i]
        $fl  = $response.hourly.apparent_temperature[$i]
        $rn  = $response.hourly.rain[$i]
        $wn  = $response.hourly.wind_speed_10m[$i]
        $pr  = $response.hourly.surface_pressure[$i]

        $rainColor = if ($rn -gt 0) { "Magenta" } else { "DarkGray" }

        Write-Host ("{0,-18} | " -f $t) -NoNewline -ForegroundColor White
        Write-Host ("{0,-10} | " -f "$tmp C") -NoNewline -ForegroundColor Green
        Write-Host ("{0,-12} | " -f "$fl C") -NoNewline -ForegroundColor DarkGreen
        Write-Host ("{0,-10} | " -f "$rn mm") -NoNewline -ForegroundColor $rainColor
        Write-Host ("{0,-10} | " -f "$wn km/h") -NoNewline -ForegroundColor Blue
        Write-Host ("{0,-12}" -f "$pr hPa") -ForegroundColor Yellow
    }
    Write-Host ""

    # 7-Day Daily Rain Sum
    Write-Host "7-DAY RAIN SUM FORECAST:" -ForegroundColor Yellow
    Write-Host ("{0,-15} | {1,-15} | {2,-30}" -f "Date", "Rain Sum (mm)", "Visual Scale") -ForegroundColor DarkYellow
    Write-Host ("-" * 65) -ForegroundColor DarkGray

    for ($d = 0; $d -lt $response.daily.time.Count; $d++) {
        $dayDate = $response.daily.time[$d]
        $dayRain = $response.daily.rain_sum[$d]
        
        $barsCount = [Math]::Min([int]($dayRain * 4), 25)
        if ($barsCount -eq 0 -and $dayRain -gt 0) { $barsCount = 1 }
        $barStr = "#" * $barsCount
        if ($dayRain -eq 0) { $barStr = ". (Dry)" }

        Write-Host ("{0,-15} | " -f $dayDate) -NoNewline -ForegroundColor White
        Write-Host ("{0,-15} | " -f "$dayRain mm") -NoNewline -ForegroundColor Cyan
        Write-Host "$barStr" -ForegroundColor Magenta
    }
    Write-Host ""
    Write-Host ("=" * 85) -ForegroundColor Cyan
}

if ($Watch) {
    Write-Host "Starting Meteo Watch Mode (Refreshing every 60 seconds... Press Ctrl+C to stop)" -ForegroundColor Yellow
    while ($true) {
        Show-Weather
        Start-Sleep -Seconds 60
    }
} else {
    Show-Weather
}
