# BUILD WITH DOCKER - Fixed version
# This avoids the root warning by passing the correct flags

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   BUILDING APK WITH DOCKER" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Docker is running
try {
    docker ps | Out-Null
    Write-Host "✅ Docker is running" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker is not running!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please start Docker Desktop and try again." -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "📦 Starting APK build..." -ForegroundColor Yellow
Write-Host "⏱️  This will take 30-60 minutes for first build" -ForegroundColor Yellow
Write-Host ""
Write-Host "The build will:" -ForegroundColor Cyan
Write-Host "  1. Download Android SDK/NDK (~2-3 GB)" -ForegroundColor White
Write-Host "  2. Compile Python for Android" -ForegroundColor White
Write-Host "  3. Build Kivy and NumPy" -ForegroundColor White
Write-Host "  4. Package your app into APK" -ForegroundColor White
Write-Host ""

$continue = Read-Host "Continue with build? (Y/n)"
if ($continue -eq 'n' -or $continue -eq 'N') {
    Write-Host "Build cancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "🚀 Building APK..." -ForegroundColor Green
Write-Host ""

# Run buildozer with proper flags to avoid root warning
docker run --rm `
    -v "${PWD}:/home/user/app" `
    -e BUILDOZER_WARN_ON_ROOT=0 `
    kivy/buildozer `
    android debug

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "   ✅ BUILD SUCCESSFUL!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "📱 Your APK is ready!" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Location:" -ForegroundColor Yellow
    Write-Host "  bin\mazeescape-1.0-arm64-v8a_armeabi-v7a-debug.apk" -ForegroundColor White
    Write-Host ""
    
    if (Test-Path "bin\*.apk") {
        $apk = Get-Item "bin\*.apk" | Select-Object -First 1
        Write-Host "APK Details:" -ForegroundColor Cyan
        Write-Host "  Name: $($apk.Name)" -ForegroundColor White
        Write-Host "  Size: $([math]::Round($apk.Length / 1MB, 2)) MB" -ForegroundColor White
        Write-Host ""
    }
    
    Write-Host "Next steps:" -ForegroundColor Yellow
    Write-Host "  1. Transfer APK to your Android device" -ForegroundColor White
    Write-Host "  2. Enable 'Install from Unknown Sources'" -ForegroundColor White
    Write-Host "  3. Install and enjoy!" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "   ❌ BUILD FAILED" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Common issues:" -ForegroundColor Yellow
    Write-Host "  1. Not enough disk space (need 5+ GB free)" -ForegroundColor White
    Write-Host "  2. Docker memory too low (increase to 4+ GB)" -ForegroundColor White
    Write-Host "  3. Network issues during SDK download" -ForegroundColor White
    Write-Host ""
    Write-Host "Try:" -ForegroundColor Cyan
    Write-Host "  - Increase Docker memory: Docker Desktop → Settings → Resources" -ForegroundColor White
    Write-Host "  - Free up disk space" -ForegroundColor White
    Write-Host "  - Check your internet connection" -ForegroundColor White
    Write-Host "  - Try GitHub Actions instead (see START_BUILD_HERE.md)" -ForegroundColor White
    Write-Host ""
}
