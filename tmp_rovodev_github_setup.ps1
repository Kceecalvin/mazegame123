# Quick GitHub Actions Setup Script

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   GITHUB ACTIONS - EASIEST METHOD" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

Write-Host "This is the FASTEST way to get your APK!" -ForegroundColor Yellow
Write-Host ""

Write-Host "Why GitHub Actions?" -ForegroundColor Cyan
Write-Host "  ✓ No local setup needed" -ForegroundColor Gray
Write-Host "  ✓ Works on any computer" -ForegroundColor Gray
Write-Host "  ✓ Free for public repositories" -ForegroundColor Gray
Write-Host "  ✓ Build happens in the cloud" -ForegroundColor Gray
Write-Host "  ✓ Takes 20-30 minutes, but you do not have to watch" -ForegroundColor Gray
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "STEP-BY-STEP INSTRUCTIONS:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "1. INITIALIZE GIT (if not already done)" -ForegroundColor Yellow
Write-Host "   Run these commands:" -ForegroundColor White
Write-Host ""
Write-Host "   git init" -ForegroundColor Cyan
Write-Host "   git add ." -ForegroundColor Cyan
Write-Host "   git commit -m `"Initial commit - Maze Escape Game`"" -ForegroundColor Cyan
Write-Host ""

Write-Host "2. CREATE GITHUB REPOSITORY" -ForegroundColor Yellow
Write-Host "   a. Go to: https://github.com/new" -ForegroundColor Cyan
Write-Host "   b. Repository name: maze-escape-game" -ForegroundColor White
Write-Host "   c. Choose Public (for free builds)" -ForegroundColor White
Write-Host "   d. Click Create repository" -ForegroundColor White
Write-Host ""

Write-Host "3. PUSH YOUR CODE TO GITHUB" -ForegroundColor Yellow
Write-Host "   GitHub will show you commands like:" -ForegroundColor White
Write-Host ""
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/maze-escape-game.git" -ForegroundColor Cyan
Write-Host "   git branch -M main" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""
Write-Host "   Note: Use YOUR_USERNAME - replace with your GitHub username!" -ForegroundColor Yellow
Write-Host ""

Write-Host "4. TRIGGER THE BUILD" -ForegroundColor Yellow
Write-Host "   a. Go to your repository on GitHub" -ForegroundColor White
Write-Host "   b. Click Actions tab at the top" -ForegroundColor White
Write-Host "   c. Click Build Android APK on the left" -ForegroundColor White
Write-Host "   d. Click Run workflow button (top right)" -ForegroundColor White
Write-Host "   e. Click green Run workflow button" -ForegroundColor White
Write-Host ""

Write-Host "5. WAIT FOR BUILD (20-30 minutes)" -ForegroundColor Yellow
Write-Host "   You can close your computer and come back later!" -ForegroundColor White
Write-Host ""

Write-Host "6. DOWNLOAD YOUR APK" -ForegroundColor Yellow
Write-Host "   a. Click on the completed workflow run" -ForegroundColor White
Write-Host "   b. Scroll to Artifacts section at the bottom" -ForegroundColor White
Write-Host "   c. Click maze-escape-apk to download" -ForegroundColor White
Write-Host "   d. Extract the ZIP file" -ForegroundColor White
Write-Host "   e. Install the APK on your Android device!" -ForegroundColor White
Write-Host ""

Write-Host "========================================" -ForegroundColor Green
Write-Host ""

Write-Host "Need help with git commands?" -ForegroundColor Yellow
Write-Host "Run these now:" -ForegroundColor White
Write-Host ""

# Check if git is installed
try {
    $gitVersion = git --version
    Write-Host "[OK] Git is installed: $gitVersion" -ForegroundColor Green
    Write-Host ""
    
    # Check if already a git repo
    if (Test-Path ".git") {
        Write-Host "[OK] Git repository already initialized" -ForegroundColor Green
    } else {
        Write-Host "[INFO] Git not initialized yet. Run: git init" -ForegroundColor Yellow
    }
    
} catch {
    Write-Host "[ERROR] Git is not installed!" -ForegroundColor Red
    Write-Host "Download from: https://git-scm.com/download/win" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Ready to start? Copy the commands above!" -ForegroundColor Green
Write-Host ""
