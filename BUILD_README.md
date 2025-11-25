# Maze Escape - APK Build Guide

This guide will help you build an Android APK for the Maze Escape game.

## Prerequisites

The Maze Escape game is built using **Kivy**, a Python framework for mobile apps. To build an Android APK, you need:

- **Linux environment** (Ubuntu/Debian recommended) or **WSL2** on Windows
- **Python 3.8+**
- **Buildozer** (APK build tool)
- **Android SDK/NDK** (downloaded automatically by Buildozer)

## Quick Start

### On Linux or WSL2:

```bash
# Make the script executable
chmod +x tmp_rovodev_build_apk.sh

# Run the build script
./tmp_rovodev_build_apk.sh
```

### On Windows (using WSL2):

1. **Install WSL2** (if not already installed):
   ```powershell
   # Run in PowerShell as Administrator
   wsl --install
   ```

2. **Open Ubuntu/WSL Terminal** from Start Menu

3. **Navigate to your project**:
   ```bash
   cd /mnt/c/Users/YourUsername/path/to/maze_game
   ```

4. **Run the build script**:
   ```bash
   chmod +x tmp_rovodev_build_apk.sh
   ./tmp_rovodev_build_apk.sh
   ```

## Manual Build Steps

If you prefer to build manually or the script doesn't work:

### 1. Install System Dependencies (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip git build-essential \
    libssl-dev libffi-dev libpython3-dev python3-setuptools \
    zip unzip openjdk-11-jdk autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 \
    cmake
```

### 2. Install Python Dependencies

```bash
pip3 install --upgrade pip
pip3 install --upgrade cython==0.29.33
pip3 install --upgrade buildozer
```

### 3. Build the APK

```bash
# Clean previous builds (optional)
buildozer android clean

# Build debug APK (first build takes 15-30 minutes)
buildozer -v android debug
```

### 4. Find Your APK

The APK will be located at:
```
bin/mazeescape-0.1-arm64-v8a-debug.apk
```

## Installing the APK on Android Device

### Method 1: Direct Transfer

1. Enable **Developer Options** on your Android device
2. Enable **Install Unknown Apps** for your file manager
3. Transfer the APK file to your device (USB, email, cloud storage, etc.)
4. Open the APK file on your device
5. Tap "Install"

### Method 2: Using ADB (Android Debug Bridge)

```bash
# Install ADB if not already installed
sudo apt-get install -y adb

# Connect your device via USB (with USB Debugging enabled)
adb devices

# Install the APK
adb install bin/mazeescape-0.1-arm64-v8a-debug.apk
```

## Buildozer Configuration

The build configuration is in `buildozer.spec`:

- **Package Name**: org.example.mazeescape
- **Version**: 0.1
- **Target API**: 33 (Android 13)
- **Min API**: 21 (Android 5.0)
- **Architecture**: arm64-v8a, armeabi-v7a
- **Requirements**: python3, kivy==2.2.1, numpy

## Building a Release APK (for Google Play Store)

To build a signed release APK:

1. **Create a keystore**:
   ```bash
   keytool -genkey -v -keystore my-release-key.keystore -alias maze_escape \
       -keyalg RSA -keysize 2048 -validity 10000
   ```

2. **Edit buildozer.spec** and add:
   ```ini
   [app]
   android.release_artifact = apk
   
   # Signing
   android.sign = True
   android.keystore = /path/to/my-release-key.keystore
   android.keystore_alias = maze_escape
   android.keystore_password = your_keystore_password
   android.key_password = your_key_password
   ```

3. **Build release**:
   ```bash
   buildozer android release
   ```

## Troubleshooting

### Build Fails with "Java not found"
```bash
sudo apt-get install -y openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

### Build Fails with "Cython version"
```bash
pip3 install --upgrade cython==0.29.33
```

### NDK/SDK Download Issues
- Check your internet connection
- Try cleaning and rebuilding: `buildozer android clean`
- Delete `.buildozer` folder and rebuild

### Out of Space
First build requires ~5-7 GB of disk space for SDK/NDK.

### Permission Denied on WSL
```bash
chmod +x tmp_rovodev_build_apk.sh
```

## Build Time Expectations

- **First Build**: 15-30 minutes (downloads SDK, NDK, dependencies)
- **Subsequent Builds**: 2-5 minutes (only rebuilds changed code)

## Additional Resources

- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Python-for-Android](https://python-for-android.readthedocs.io/)

## Project Structure

```
maze_game/
├── main.py                 # Main Kivy app
├── maze_generator.py       # Maze generation algorithms
├── maze_solver.py          # Pathfinding algorithms
├── maze_snake.py           # Enemy snake logic
├── buildozer.spec          # Build configuration
├── tmp_rovodev_build_apk.sh    # Build script (Linux/WSL)
├── tmp_rovodev_build_apk.ps1   # Build helper (Windows)
└── BUILD_README.md         # This file
```

## Support

If you encounter issues:
1. Check the error messages in the buildozer output
2. Search for the error on [Buildozer GitHub Issues](https://github.com/kivy/buildozer/issues)
3. Check [Kivy Discord](https://chat.kivy.org/) or [Stack Overflow](https://stackoverflow.com/questions/tagged/buildozer)

---

**Happy Building! 🎮**
