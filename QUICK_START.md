# 🎮 Maze Escape - Quick Start Guide to Build APK

Choose the method that works best for you:

---

## 🚀 Option 1: GitHub Actions (EASIEST - No Setup Required!)

**Best for:** Anyone with a GitHub account, works on any OS

### Steps:
1. Create a GitHub repository
2. Push your code: 
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```
3. Go to GitHub → Actions tab → Run workflow
4. Wait 20-30 minutes
5. Download APK from Artifacts section

📖 **Detailed Guide:** See `GITHUB_ACTIONS_BUILD.md`

---

## 🐳 Option 2: Docker (Easy - If You Have Docker)

**Best for:** Windows/Mac users with Docker Desktop installed

### Steps:
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Run the build script:
   
   **Windows (PowerShell):**
   ```powershell
   .\tmp_rovodev_docker_build.ps1
   ```
   
   **Linux/Mac:**
   ```bash
   chmod +x tmp_rovodev_docker_build.sh
   ./tmp_rovodev_docker_build.sh
   ```

3. Wait 20-30 minutes
4. Find APK in `bin/` folder

---

## 🐧 Option 3: WSL2 on Windows (Recommended for Local Builds)

**Best for:** Windows users who want local builds

### Steps:
1. Install WSL2:
   ```powershell
   # In PowerShell as Administrator
   wsl --install
   ```

2. Open Ubuntu from Start Menu

3. Navigate to your project:
   ```bash
   cd /mnt/c/Users/YourUsername/path/to/maze_game
   ```

4. Run build script:
   ```bash
   chmod +x tmp_rovodev_build_apk.sh
   ./tmp_rovodev_build_apk.sh
   ```

5. Wait 20-30 minutes
6. Find APK in `bin/` folder

📖 **Detailed Guide:** See `BUILD_INSTRUCTIONS_WSL.txt`

---

## 🖥️ Option 4: Native Linux

**Best for:** Linux users

### Steps:
1. Run build script:
   ```bash
   chmod +x tmp_rovodev_build_apk.sh
   ./tmp_rovodev_build_apk.sh
   ```

2. Wait 20-30 minutes
3. Find APK in `bin/` folder

---

## 📱 Installing APK on Your Android Device

Once you have the APK:

### Method 1: Direct Install
1. Transfer APK to your phone (USB, email, cloud, etc.)
2. Go to **Settings → Security → Install Unknown Apps**
3. Enable for your file manager
4. Tap the APK file → Install

### Method 2: ADB (Developer Method)
```bash
adb install bin/mazeescape-0.1-arm64-v8a-debug.apk
```

---

## 📊 Comparison Table

| Method | Setup Time | Build Time | Difficulty | Cost |
|--------|------------|------------|------------|------|
| GitHub Actions | 5 min | 20-30 min | ⭐ Easy | Free |
| Docker | 10 min | 20-30 min | ⭐⭐ Medium | Free |
| WSL2 | 15 min | 20-30 min | ⭐⭐ Medium | Free |
| Native Linux | 0 min | 20-30 min | ⭐⭐⭐ Advanced | Free |

---

## ❓ Which Option Should I Choose?

- **I just want an APK quickly** → GitHub Actions
- **I have Docker and want local builds** → Docker
- **I'm on Windows and want control** → WSL2
- **I'm on Linux** → Native Linux

---

## 🐛 Troubleshooting

### Build Fails?
- Check error messages in the logs
- Ensure stable internet connection (downloads ~2GB on first build)
- Try cleaning and rebuilding: `buildozer android clean`

### Can't Install APK?
- Enable "Unknown Sources" in Android settings
- Check if APK is for correct architecture (arm64 or arm)
- Make sure Android version is 5.0+ (API 21+)

### Need More Help?
- Read the full guide: `BUILD_README.md`
- Check GitHub Actions logs (if using GitHub)
- Search error messages on Stack Overflow

---

## 📦 What Gets Built?

**File:** `bin/mazeescape-0.1-arm64-v8a-debug.apk`
- **Size:** ~20-30 MB
- **Type:** Debug APK (not for Play Store)
- **Compatible:** Android 5.0+ (API 21+)
- **Architecture:** ARM64 and ARMv7

---

## 🎯 Next Steps After Building

1. **Test the APK** on your device
2. **Build a release version** for Play Store (see BUILD_README.md)
3. **Add custom icons** (edit buildozer.spec)
4. **Version your app** (increment version in buildozer.spec)

---

## 📚 Additional Documentation

- `BUILD_README.md` - Complete build guide
- `GITHUB_ACTIONS_BUILD.md` - GitHub Actions detailed guide
- `buildozer.spec` - Build configuration file

---

**Ready to build? Pick an option above and let's go! 🚀**
