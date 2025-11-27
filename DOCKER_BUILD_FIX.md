# Docker Build - Fixed Command

## The Problem

The original Docker command was failing with:
```
Buildozer is running as root!
Are you sure you want to continue [y/n]? 
EOFError: EOF when reading a line
```

This happens because Docker can't read interactive input.

## The Solution

### Option 1: Use the Fixed Script (Easiest)

```powershell
.\BUILD_WITH_DOCKER.ps1
```

This script:
- Checks Docker is running
- Sets the environment variable to skip root warning
- Shows progress information
- Handles errors properly

### Option 2: Manual Command (Fixed)

```powershell
docker run --rm -v "${PWD}:/home/user/app" -e BUILDOZER_WARN_ON_ROOT=0 kivy/buildozer android debug
```

The key fix: `-e BUILDOZER_WARN_ON_ROOT=0` disables the root warning

### Option 3: Alternative Docker Image

Try the official GitHub Container Registry image:

```powershell
docker run --rm -v "${PWD}:/app" ghcr.io/kivy/buildozer:latest bash -c "cd /app && buildozer android debug"
```

## Build Requirements

- **Docker Desktop** installed and running
- **Disk Space:** 5+ GB free
- **RAM:** 4+ GB allocated to Docker
- **Time:** 30-60 minutes (first build)

## Configure Docker Resources

If build fails with memory errors:

1. Open **Docker Desktop**
2. Go to **Settings** → **Resources**
3. Set **Memory** to at least **4 GB**
4. Set **Disk** to at least **10 GB**
5. Click **Apply & Restart**

## Expected Output

After successful build:
```
bin/mazeescape-1.0-arm64-v8a_armeabi-v7a-debug.apk
```

Size: ~15-20 MB

## Alternative: GitHub Actions

If Docker continues to have issues, **GitHub Actions is easier**:

1. Run: `.\BUILD_APK_NOW.ps1`
2. Wait 30-60 minutes
3. Download APK from GitHub Actions artifacts

No local setup required! ✅

---

**Recommendation:** Use GitHub Actions for most reliable builds.
