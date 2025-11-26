# Build APK using Docker
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Building Maze Escape APK" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if Docker is running
Write-Host "Checking Docker status..." -ForegroundColor Yellow
$dockerInfo = docker info 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker is not running. Starting Docker Desktop..." -ForegroundColor Red
    Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    Write-Host "Waiting for Docker to start (30 seconds)..." -ForegroundColor Yellow
    Start-Sleep -Seconds 30
}

Write-Host "Docker is ready!" -ForegroundColor Green
Write-Host ""

# Build using buildozer in Docker container
Write-Host "Building APK with Buildozer (this takes 15-30 minutes)..." -ForegroundColor Yellow
Write-Host "Progress will be shown below:" -ForegroundColor Gray
Write-Host ""

# Use the official buildozer Docker image
docker run --rm -v "${PWD}:/app" kivy/buildozer android debug

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "================================" -ForegroundColor Green
    Write-Host "BUILD SUCCESSFUL!" -ForegroundColor Green
    Write-Host "================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "APK Location: bin\maze-escape-*.apk" -ForegroundColor Cyan
    if (Test-Path "bin\*.apk") {
        Get-ChildItem bin\*.apk | ForEach-Object {
            Write-Host "  -> $($_.Name) ($([math]::Round($_.Length/1MB, 2)) MB)" -ForegroundColor White
        }
    }
} else {
    Write-Host ""
    Write-Host "================================" -ForegroundColor Red
    Write-Host "BUILD FAILED!" -ForegroundColor Red
    Write-Host "================================" -ForegroundColor Red
}
