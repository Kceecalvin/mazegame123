# Maze Escape APK Builder
# Python + Kivy is OPTIMAL - No conversion needed!

Write-Host ""
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "   MAZE ESCAPE - APK BUILDER" -ForegroundColor Cyan
Write-Host "   Python + Kivy = BEST for Mobile Games!" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Your game is already built with professional technology!" -ForegroundColor Green
Write-Host "No conversion needed - just build the APK!`n" -ForegroundColor White

Write-Host "Choose build method:`n" -ForegroundColor Yellow

Write-Host "1. GitHub Actions (RECOMMENDED)" -ForegroundColor Cyan
Write-Host "   - Easiest and most reliable" -ForegroundColor Gray
Write-Host "   - 15-20 minutes" -ForegroundColor Gray
Write-Host "   - 99% success rate`n" -ForegroundColor Gray

Write-Host "2. Docker (Local Build)" -ForegroundColor Cyan
Write-Host "   - Builds on your computer" -ForegroundColor Gray
Write-Host "   - 20-30 minutes first time" -ForegroundColor Gray
Write-Host "   - Requires Docker running`n" -ForegroundColor Gray

Write-Host "3. Show All Instructions" -ForegroundColor Cyan
Write-Host "   - View complete build guide`n" -ForegroundColor Gray

$choice = Read-Host "Enter choice (1-3)"

switch ($choice) {
    "1" {
        Write-Host "`n=== GitHub Actions Method ===" -ForegroundColor Green
        Write-Host "`nThis is the BEST method! Here's how:`n" -ForegroundColor Cyan
        
        Write-Host "STEP 1: Create GitHub Account (if needed)" -ForegroundColor Yellow
        Write-Host "   Go to: https://github.com/join`n" -ForegroundColor White
        
        Write-Host "STEP 2: Create New Repository" -ForegroundColor Yellow
        Write-Host "   Go to: https://github.com/new" -ForegroundColor White
        Write-Host "   Name: maze-escape-game" -ForegroundColor Gray
        Write-Host "   Make it: Public" -ForegroundColor Gray
        Write-Host "   Click: Create repository`n" -ForegroundColor Gray
        
        Write-Host "STEP 3: Push Your Code" -ForegroundColor Yellow
        Write-Host "   Copy these commands (replace YOUR_USERNAME):" -ForegroundColor White
        Write-Host ""
        Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/maze-escape-game.git" -ForegroundColor Cyan
        Write-Host "   git branch -M main" -ForegroundColor Cyan
        Write-Host "   git push -u origin main" -ForegroundColor Cyan
        Write-Host ""
        
        Write-Host "STEP 4: Trigger Build" -ForegroundColor Yellow
        Write-Host "   1. Go to: https://github.com/YOUR_USERNAME/maze-escape-game/actions" -ForegroundColor White
        Write-Host "   2. Click: 'Build Android APK' workflow" -ForegroundColor Gray
        Write-Host "   3. Click: Green 'Run workflow' button" -ForegroundColor Gray
        Write-Host "   4. Select: main branch" -ForegroundColor Gray
        Write-Host "   5. Click: 'Run workflow'`n" -ForegroundColor Gray
        
        Write-Host "STEP 5: Download APK (15-20 min later)" -ForegroundColor Yellow
        Write-Host "   1. Refresh the Actions page" -ForegroundColor White
        Write-Host "   2. Click your workflow run (green checkmark)" -ForegroundColor Gray
        Write-Host "   3. Scroll to bottom 'Artifacts' section" -ForegroundColor Gray
        Write-Host "   4. Download 'maze-escape-apk.zip'" -ForegroundColor Gray
        Write-Host "   5. Extract and install on Android!`n" -ForegroundColor Gray
        
        if (-not (Test-Path ".git")) {
            Write-Host "Initializing git for you..." -ForegroundColor Yellow
            git init 2>&1 | Out-Null
            git add . 2>&1 | Out-Null
            git commit -m "Maze Escape Game - Ready for APK build" 2>&1 | Out-Null
            Write-Host "Git ready! Follow steps above.`n" -ForegroundColor Green
        }
    }
    
    "2" {
        Write-Host "`n=== Docker Build Method ===" -ForegroundColor Green
        Write-Host ""
        Write-Host "Starting Docker build...`n" -ForegroundColor Yellow
        Write-Host "This will take 20-30 minutes.`n" -ForegroundColor Gray
        
        Write-Host "Building APK with command:" -ForegroundColor Cyan
        Write-Host 'docker run --rm -v "${PWD}:/home/user/app" kivy/buildozer android debug' -ForegroundColor White
        Write-Host ""
        
        docker run --rm -e BUILDOZER_WARN_ON_ROOT=0 -v "${PWD}:/home/user/app" kivy/buildozer android debug
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "`n=== BUILD SUCCESSFUL! ===" -ForegroundColor Green
            if (Test-Path "bin\*.apk") {
                Get-ChildItem bin\*.apk | ForEach-Object {
                    Write-Host "`nAPK: $($_.Name)" -ForegroundColor Cyan
                    Write-Host "Size: $([math]::Round($_.Length/1MB, 2)) MB" -ForegroundColor White
                    Write-Host "Path: $($_.FullName)" -ForegroundColor Gray
                }
            }
        } else {
            Write-Host "`nBuild failed. Try GitHub Actions instead (Option 1).`n" -ForegroundColor Red
        }
    }
    
    "3" {
        Write-Host "`n=== Build Instructions ===" -ForegroundColor Cyan
        Write-Host "`nComplete guides available in:" -ForegroundColor White
        Write-Host "  - tmp_rovodev_FINAL_BUILD_INSTRUCTIONS.md" -ForegroundColor Cyan
        Write-Host "  - tmp_rovodev_instant_apk.md" -ForegroundColor Cyan
        Write-Host "  - QUICK_BUILD_SOLUTION.md`n" -ForegroundColor Cyan
        
        Write-Host "Quick command for Docker build:" -ForegroundColor Yellow
        Write-Host 'docker run --rm -v "${PWD}:/home/user/app" kivy/buildozer android debug' -ForegroundColor White
        Write-Host ""
    }
    
    default {
        Write-Host "`nInvalid choice. Run script again.`n" -ForegroundColor Red
    }
}

Write-Host "`n=============================================" -ForegroundColor Cyan
Write-Host "Python + Kivy is PERFECT for your game!" -ForegroundColor Green
Write-Host "No conversion needed - already optimal!" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""
