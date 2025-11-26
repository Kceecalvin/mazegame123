# 📱 Maze Escape - Complete APK Build Guide

## 🎮 About Your Game

**Language:** Python with Kivy Framework  
**Why Kivy?** One of the BEST choices for mobile game development because:
- ✅ Cross-platform (Android, iOS, Windows, Mac, Linux)
- ✅ Perfect for 2D games like this maze game
- ✅ Excellent touch/gesture support
- ✅ OpenGL-accelerated rendering
- ✅ Single codebase for all platforms
- ✅ Large community and mature framework

## 🔨 Current Build Status

**Docker build is now running in the background!**

The build process typically takes **20-30 minutes** for the first build because it needs to:
1. Download Android SDK (~500MB)
2. Download Android NDK (~1GB)
3. Compile Python for Android
4. Compile Kivy
5. Package your game into APK

**Subsequent builds are much faster (5-10 minutes).**

## 📊 How to Check Build Progress

Run this command to see current progress:
```powershell
Get-Process -Name docker | Select-Object CPU, WS
```

Or check Docker Desktop logs in the GUI.

## 📁 Where Will the APK Be?

After the build completes, your APK will be located at:
```
bin/mazeescape-0.1-arm64-v8a_armeabi-v7a-debug.apk
```

File size will be approximately **25-35 MB**.

## 🚀 Three Ways to Build Your APK

### ✅ Method 1: Docker (Currently Running)
**Status:** In progress  
**Time:** 20-30 minutes first time, 5-10 minutes after  
**Pros:** Reliable, works on Windows  
**Cons:** Large downloads, slow first time  

Command:
```powershell
docker run --rm -v "${PWD}:/home/user/app" kivy/buildozer android debug
```

---

### ✅ Method 2: GitHub Actions (Easiest - Recommended)
**Status:** Ready to use  
**Time:** 15-20 minutes  
**Pros:** No local setup, automatic, free  
**Cons:** Requires GitHub account  

Steps:
1. **Push to GitHub** (if not already):
   ```bash
   git init
   git add .
   git commit -m "Ready to build APK"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/maze-escape-game.git
   git push -u origin main
   ```

2. **Trigger Build**:
   - Go to: `https://github.com/YOUR_USERNAME/maze-escape-game/actions`
   - Click "Build Android APK" workflow
   - Click "Run workflow" → Select "main" → Click green "Run workflow"

3. **Download APK**:
   - Wait 15-20 minutes
   - Refresh the page
   - Click on the completed run
   - Scroll to "Artifacts" section
   - Download "maze-escape-apk.zip"
   - Extract to get your APK

---

### ✅ Method 3: WSL2 + Ubuntu (Alternative)
**Status:** Available but requires OneDrive workaround  
**Time:** 20-30 minutes first time  
**Pros:** Native Linux experience  
**Cons:** Path issues with OneDrive  

Steps:
1. Copy project to a non-OneDrive location (e.g., `C:\Projects\maze_project`)
2. Open WSL2:
   ```bash
   cd /mnt/c/Projects/maze_project
   buildozer android debug
   ```

---

## 📲 Installing the APK on Your Phone

### For Android Devices:

1. **Enable Developer Options**:
   - Go to Settings → About Phone
   - Tap "Build Number" 7 times
   - Go back to Settings → Developer Options
   - Enable "USB Debugging"

2. **Install via USB**:
   ```powershell
   # Connect phone via USB
   adb install bin/mazeescape-0.1-arm64-v8a_armeabi-v7a-debug.apk
   ```

3. **Install Manually**:
   - Copy APK to phone
   - Open file manager on phone
   - Tap the APK file
   - Allow installation from unknown sources
   - Install!

---

## 🎯 Game Features

Your maze game includes:
- ✅ 10 progressive levels
- ✅ Touch controls (swipe gestures)
- ✅ Arrow button controls
- ✅ Smart enemy snake with AI
- ✅ Hint system
- ✅ Move counter and timer
- ✅ Mobile-optimized UI

---

## ⚙️ Build Configuration (buildozer.spec)

Current settings:
- **Package Name:** `org.example.mazeescape`
- **Version:** 0.1
- **Orientation:** Portrait
- **Min Android:** 5.0 (API 21)
- **Target Android:** 13 (API 33)
- **Architectures:** ARM64-v8a, ARMv7a
- **Permissions:** INTERNET, VIBRATE, WAKE_LOCK

---

## 🐛 Troubleshooting

### Docker Build Issues:
- **"Docker not running"**: Start Docker Desktop manually
- **"Permission denied"**: Run as Administrator
- **Build fails**: Check logs with `docker logs CONTAINER_ID`

### GitHub Actions Issues:
- **Build fails**: Check Actions tab for error logs
- **No artifacts**: Wait until build completes (green checkmark)

### Installation Issues:
- **"App not installed"**: Enable "Install unknown apps" in Settings
- **"Parse error"**: Wrong architecture (try universal build)

---

## 📝 Next Steps After Build

1. **Test on Device**: Install and play!
2. **Get Feedback**: Share with friends
3. **Iterate**: Fix bugs and add features
4. **Release**: Publish to Google Play Store

---

## 🎨 Want to Customize?

Edit these files:
- `main.py` - Game logic
- `maze_game.kv` - UI layout (Kivy language)
- `buildozer.spec` - Build configuration
- Colors, levels, difficulty in `main.py`

---

## 📞 Build Commands Quick Reference

```powershell
# Docker build
docker run --rm -v "${PWD}:/home/user/app" kivy/buildozer android debug

# Clean build (if issues)
docker run --rm -v "${PWD}:/home/user/app" kivy/buildozer android clean

# Release build (for Play Store)
docker run --rm -v "${PWD}:/home/user/app" kivy/buildozer android release
```

---

**Your build is currently running! Check back in 20-30 minutes. 🎉**
