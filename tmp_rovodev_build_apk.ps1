# PowerShell script to build APK for Maze Escape Game
# This script helps build the Android APK using Buildozer

Write-Host "=== Maze Escape APK Builder ===" -ForegroundColor Green
Write-Host ""

# Check if running on Windows
if ($IsWindows -or $env:OS -match "Windows") {
    Write-Host "WARNING: Buildozer does not run natively on Windows!" -ForegroundColor Red
    Write-Host ""
    Write-Host "You have the following options:" -ForegroundColor Yellow
    Write-Host "1. Use WSL (Windows Subsystem for Linux) - RECOMMENDED"
    Write-Host "2. Use a Linux Virtual Machine"
    Write-Host "3. Use a cloud build service like GitHub Actions"
    Write-Host "4. Use a Linux machine directly"
    Write-Host ""
    Write-Host "To use WSL:" -ForegroundColor Cyan
    Write-Host "  1. Install WSL2 with Ubuntu: wsl --install"
    Write-Host "  2. Open Ubuntu from Start Menu"
    Write-Host "  3. Navigate to your project: cd /mnt/c/path/to/your/project"
    Write-Host "  4. Run: bash tmp_rovodev_build_apk.sh"
    Write-Host ""
    
    # Create WSL instructions file
    $wslInstructions = @"
# WSL Build Instructions for Maze Escape

## Step 1: Install WSL2 (if not already installed)
Open PowerShell as Administrator and run:
``````
wsl --install
``````

## Step 2: Open Ubuntu/WSL Terminal
Search for "Ubuntu" in Start Menu and open it

## Step 3: Navigate to your project
``````bash
cd /mnt/c/Users/YourUsername/path/to/maze_game
``````

## Step 4: Run the build script
``````bash
bash tmp_rovodev_build_apk.sh
``````

The script will:
- Install all required dependencies
- Set up Buildozer
- Build the APK
- Output the APK to bin/ directory
"@
    
    $wslInstructions | Out-File -FilePath "BUILD_INSTRUCTIONS_WSL.txt" -Encoding UTF8
    Write-Host "Created BUILD_INSTRUCTIONS_WSL.txt for detailed WSL setup instructions" -ForegroundColor Green
    
} else {
    Write-Host "Error: This script is designed for Windows. On Linux/Mac, use the bash script instead." -ForegroundColor Red
}

Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
