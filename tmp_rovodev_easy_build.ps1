# Easy APK Build Script for Windows
# This script tries multiple methods to build your APK

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Maze Escape - APK Builder for Windows" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Method 1: Try Docker (if running)
Write-Host "Method 1: Trying Docker..." -ForegroundColor Yellow
$dockerRunning = docker ps 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Docker is running!" -ForegroundColor Green
    Write-Host "Building APK with Docker (this takes 20-30 minutes)..." -ForegroundColor Yellow
    Write-Host ""
    
    docker run --rm -v "${PWD}:/home/user/app" kivy/buildozer android debug
    
    if ($LASTEXITCODE -eq 0 -and (Test-Path "bin\*.apk")) {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Green
        Write-Host "       BUILD SUCCESSFUL!" -ForegroundColor Green
        Write-Host "========================================" -ForegroundColor Green
        Write-Host ""
        Get-ChildItem bin\*.apk | ForEach-Object {
            Write-Host "APK: $($_.Name) - Size: $([math]::Round($_.Length/1MB, 2)) MB" -ForegroundColor Cyan
            Write-Host "Location: $($_.FullName)" -ForegroundColor White
        }
        exit 0
    }
}

Write-Host "[FAILED] Docker method failed or not available" -ForegroundColor Red
Write-Host ""

# Method 2: GitHub Actions Reminder
Write-Host "Method 2: GitHub Actions (Recommended)" -ForegroundColor Yellow
Write-Host ""
Write-Host "Your project has automated builds! To build APK:" -ForegroundColor White
Write-Host "  1. Push code to GitHub" -ForegroundColor Gray
Write-Host "  2. Go to Actions tab" -ForegroundColor Gray
Write-Host "  3. Run Build Android APK workflow" -ForegroundColor Gray
Write-Host "  4. Download APK from artifacts after 15-20 minutes" -ForegroundColor Gray
Write-Host ""
Write-Host "See tmp_rovodev_github_instructions.md for details" -ForegroundColor Cyan
Write-Host ""

# Method 3: Manual Docker command
Write-Host "Method 3: Manual Docker Command" -ForegroundColor Yellow
Write-Host ""
Write-Host "If Docker Desktop is installed but not running:" -ForegroundColor White
Write-Host "  1. Start Docker Desktop manually" -ForegroundColor Gray
Write-Host "  2. Wait for it to fully start" -ForegroundColor Gray
Write-Host "  3. Run this command:" -ForegroundColor Gray
Write-Host ""
Write-Host '     docker run --rm -v "${PWD}:/home/user/app" kivy/buildozer android debug' -ForegroundColor Cyan
Write-Host ""

# Summary
Write-Host "========================================" -ForegroundColor Yellow
Write-Host "SUMMARY:" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Yellow
Write-Host "Windows does not support buildozer natively" -ForegroundColor White
Write-Host "Docker or GitHub Actions are required" -ForegroundColor White
Write-Host "GitHub Actions is easiest (no local setup needed)" -ForegroundColor Green
Write-Host "Docker works but needs to be running first" -ForegroundColor Yellow
Write-Host ""
