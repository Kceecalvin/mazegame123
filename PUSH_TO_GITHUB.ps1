# Push to GitHub and Build APK - Simple Version

Write-Host ""
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "  GITHUB ACTIONS - BUILD YOUR APK" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Python + Kivy is OPTIMAL - No conversion needed!" -ForegroundColor Green
Write-Host ""

# Check git status
if (-not (Test-Path ".git")) {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    git init
    git add .
    git commit -m "Maze Escape Game - Build APK with GitHub Actions"
    Write-Host "[OK] Git initialized!`n" -ForegroundColor Green
} else {
    Write-Host "[OK] Git already initialized`n" -ForegroundColor Green
}

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "STEP-BY-STEP INSTRUCTIONS:" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "STEP 1: Create GitHub Repository" -ForegroundColor Yellow
Write-Host "  1. Go to: https://github.com/new" -ForegroundColor White
Write-Host "  2. Repository name: maze-escape-game" -ForegroundColor White
Write-Host "  3. Make it Public (required for free Actions)" -ForegroundColor White
Write-Host "  4. DON'T check 'Initialize with README'" -ForegroundColor White
Write-Host "  5. Click 'Create repository'" -ForegroundColor White
Write-Host ""

Write-Host "STEP 2: Get Your Repository URL" -ForegroundColor Yellow
Write-Host "  After creating, copy the repository URL." -ForegroundColor White
Write-Host "  It looks like: https://github.com/YOUR_USERNAME/maze-escape-game.git" -ForegroundColor Gray
Write-Host ""

Write-Host "Enter your GitHub repository URL:" -ForegroundColor Yellow
$repoUrl = Read-Host "URL"

if ($repoUrl) {
    Write-Host ""
    Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
    
    # Add or update remote
    $remoteExists = git remote 2>&1 | Select-String "origin"
    if ($remoteExists) {
        git remote set-url origin $repoUrl
    } else {
        git remote add origin $repoUrl
    }
    
    # Push
    git branch -M main
    git push -u origin main
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[SUCCESS] Code pushed to GitHub!`n" -ForegroundColor Green
        
        Write-Host "=============================================" -ForegroundColor Green
        Write-Host "NOW BUILD YOUR APK:" -ForegroundColor Green
        Write-Host "=============================================" -ForegroundColor Green
        Write-Host ""
        
        Write-Host "STEP 3: Trigger Build on GitHub" -ForegroundColor Yellow
        Write-Host "  1. Go to your repository on GitHub" -ForegroundColor White
        Write-Host "  2. Click 'Actions' tab at the top" -ForegroundColor White
        Write-Host "  3. Click 'Build Android APK' workflow" -ForegroundColor White
        Write-Host "  4. Click 'Run workflow' button (green, on right)" -ForegroundColor White
        Write-Host "  5. Select branch: main" -ForegroundColor White
        Write-Host "  6. Click 'Run workflow'" -ForegroundColor White
        Write-Host ""
        
        Write-Host "STEP 4: Wait 15-20 Minutes" -ForegroundColor Yellow
        Write-Host "  Build will run automatically" -ForegroundColor White
        Write-Host "  Green checkmark = Success!" -ForegroundColor Green
        Write-Host ""
        
        Write-Host "STEP 5: Download APK" -ForegroundColor Yellow
        Write-Host "  1. Click on your completed workflow run" -ForegroundColor White
        Write-Host "  2. Scroll to bottom of page" -ForegroundColor White
        Write-Host "  3. Find 'Artifacts' section" -ForegroundColor White
        Write-Host "  4. Download 'maze-escape-apk.zip'" -ForegroundColor White
        Write-Host "  5. Extract and install on Android!" -ForegroundColor Green
        Write-Host ""
        
        # Extract username and repo if possible
        if ($repoUrl -match "github\.com[:/](.+?)/(.+?)(\.git)?$") {
            $username = $matches[1]
            $repoName = $matches[2]
            
            Write-Host "=============================================" -ForegroundColor Cyan
            Write-Host "QUICK LINK TO YOUR ACTIONS:" -ForegroundColor Yellow
            $actionsUrl = "https://github.com/$username/$repoName/actions"
            Write-Host $actionsUrl -ForegroundColor Cyan
            Write-Host "=============================================" -ForegroundColor Cyan
            Write-Host ""
            
            $openBrowser = Read-Host "Open GitHub Actions in browser? (y/n)"
            if ($openBrowser -eq "y") {
                Start-Process $actionsUrl
                Write-Host "[OK] Browser opened!`n" -ForegroundColor Green
            }
        }
        
        Write-Host ""
        Write-Host "Your APK will be ready in about 20 minutes!" -ForegroundColor Green
        Write-Host ""
        
    } else {
        Write-Host "[FAILED] Push failed.`n" -ForegroundColor Red
        Write-Host "This might be due to authentication." -ForegroundColor Yellow
        Write-Host "Try running manually:" -ForegroundColor Yellow
        Write-Host "  git push -u origin main" -ForegroundColor Cyan
        Write-Host ""
    }
} else {
    Write-Host ""
    Write-Host "No URL entered. Run the script again." -ForegroundColor Red
    Write-Host ""
}

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "Remember: Python + Kivy is perfect!" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""
