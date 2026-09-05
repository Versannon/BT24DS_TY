# ==============================================================================
# Localhost Web Server Launcher for Open-Meteo Weather Dashboard
# Serves http://localhost:8080/
# ==============================================================================

[CmdletBinding()]
param(
    [int]$Port = 8080
)

$Folder = $PSScriptRoot
if (-not $Folder) { $Folder = Get-Location }

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " 🌤️  LAUNCHING OPEN-METEO WEATHER DASHBOARD ON LOCALHOST" -ForegroundColor White
Write-Host " Root Directory : $Folder" -ForegroundColor DarkGray
Write-Host " Target URL      : http://localhost:$Port/" -ForegroundColor Yellow
Write-Host "================================================================================" -ForegroundColor Cyan

# Check if Python is available for a lightweight static HTTP server
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCmd) {
    Write-Host "[INFO] Using Python http.server module on port $Port..." -ForegroundColor Green
    Start-Process "http://localhost:$Port/"
    python -m http.server $Port --directory "$Folder"
    exit 0
}

# Fallback: Simple PowerShell HttpListener server
Write-Host "[INFO] Python not found. Starting native PowerShell HTTP listener on port $Port..." -ForegroundColor Yellow

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$Port/")
$listener.Start()

Write-Host "[SUCCESS] Localhost Web Server running at http://localhost:$Port/" -ForegroundColor Green
Write-Host "Press Ctrl+C in this terminal window to stop the server." -ForegroundColor DarkGray
Write-Host ""

Start-Process "http://localhost:$Port/"

try {
    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        $relPath = $request.Url.LocalPath.TrimStart('/')
        if (-not $relPath) { $relPath = "index.html" }

        $filePath = Join-Path $Folder $relPath

        if (Test-Path $filePath -PathType Leaf) {
            $bytes = [System.IO.File]::ReadAllBytes($filePath)
            $ext = [System.IO.Path]::GetExtension($filePath).ToLower()
            
            switch ($ext) {
                ".html" { $response.ContentType = "text/html; charset=utf-8" }
                ".css"  { $response.ContentType = "text/css; charset=utf-8" }
                ".js"   { $response.ContentType = "application/javascript; charset=utf-8" }
                ".json" { $response.ContentType = "application/json; charset=utf-8" }
                default { $response.ContentType = "application/octet-stream" }
            }

            $response.ContentLength64 = $bytes.Length
            $response.OutputStream.Write($bytes, 0, $bytes.Length)
        } else {
            $response.StatusCode = 404
            $buffer = [System.Text.Encoding]::UTF8.GetBytes("404 Not Found")
            $response.ContentLength64 = $buffer.Length
            $response.OutputStream.Write($buffer, 0, $buffer.Length)
        }

        $response.Close()
    }
}
finally {
    $listener.Stop()
}
