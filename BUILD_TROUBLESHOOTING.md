# 🔧 Build Troubleshooting Guide

If your GitHub Actions build fails, here are common issues and solutions:

## ❌ Common Build Errors

### 1. "Buildozer: command not found"
**Cause:** Buildozer installation failed  
**Solution:** Already handled in workflow - installs buildozer automatically

### 2. "Java not found" or "JDK not installed"
**Cause:** Java Development Kit missing  
**Solution:** Already handled in workflow - installs openjdk-11-jdk

### 3. "SDK/NDK download failed"
**Cause:** Network timeout or corrupted download  
**Solution:** 
- Re-run the workflow (builds are not always perfect first time)
- GitHub Actions will retry automatically

### 4. "Cython compilation failed"
**Cause:** Wrong Cython version  
**Solution:** Already handled - workflow installs cython==0.29.33

### 5. "Permission denied" errors
**Cause:** File permissions in build environment  
**Solution:** Already handled - workflow runs with proper permissions

### 6. Build times out after 6 hours
**Cause:** Extremely rare, usually network issues  
**Solution:** Re-run the workflow

## ✅ Successful Build Indicators

When the build succeeds, you'll see:
- ✅ Green checkmark on the workflow run
- "Build APK with Buildozer" step shows: "APK built successfully!"
- "Upload APK artifact" step completes
- "Artifacts" section appears at the bottom with "maze-escape-apk"

## 📊 Build Progress Timeline

| Time    | Step | What's Happening |
|---------|------|------------------|
| 0-2 min | Setup | Installing system dependencies |
| 2-5 min | Python | Installing Python packages |
| 5-15 min | SDK/NDK | Downloading Android SDK/NDK (~2GB) |
| 15-25 min | Build | Compiling Python, building APK |
| 25-30 min | Upload | Packaging and uploading APK |

## 🔍 How to Read Build Logs

1. Click on the workflow run
2. Click on "build" job
3. Expand each step to see logs
4. Look for:
   - ✅ Green checkmarks = Success
   - ❌ Red X = Failed (read the error message)
   - 🟡 Yellow spinner = In progress

## 🐛 Debug Mode

If build fails repeatedly, you can enable debug mode:

1. Go to your repo Settings → Secrets and variables → Actions
2. Add a new secret:
   - Name: `ACTIONS_STEP_DEBUG`
   - Value: `true`
3. Re-run the workflow for detailed logs

## 📱 APK Installation Issues

### "App not installed"
**Causes:**
- Incompatible architecture (need ARM device)
- Android version too old (need 5.0+)
- Corrupted APK download

**Solutions:**
- Check device: Settings → About Phone → Processor (should be ARM)
- Update Android if below 5.0
- Re-download APK, ensure complete download

### "Parse error"
**Cause:** Corrupted APK file  
**Solution:** 
- Re-download APK from GitHub
- Ensure ZIP is fully extracted
- Try different file manager app

### "Unknown sources blocked"
**Solution:**
1. Go to Settings → Security
2. Enable "Unknown sources" or "Install unknown apps"
3. Allow installation from your file manager

## 🔄 Re-running Failed Builds

If a build fails:
1. Check the error in the logs
2. If it's a network/timeout issue, just re-run
3. Click "Re-run failed jobs" button
4. Or click "Re-run all jobs"

## 💡 Tips for Faster Builds

1. **First build is slowest** (20-30 min) - downloads everything
2. **Subsequent builds are faster** (2-5 min) - caches dependencies
3. **Don't cancel builds** - let them complete or fail naturally
4. **Check GitHub Actions quota** - Free tier has limits

## 📞 Getting Help

If you're stuck:

1. **Check the logs** - Most errors are explained in the output
2. **Search the error** - Copy exact error message and search:
   - Google: "buildozer [error message]"
   - GitHub Issues: https://github.com/kivy/buildozer/issues
3. **Common resources:**
   - Buildozer docs: https://buildozer.readthedocs.io/
   - Kivy Discord: https://chat.kivy.org/
   - Stack Overflow: Tag `buildozer` or `kivy`

## ✅ Verify Successful Build

Before installing on phone, verify APK:
1. APK file size should be ~20-30 MB
2. File name: `mazeescape-0.1-arm64-v8a-debug.apk`
3. Can be opened with any ZIP tool (APK is a ZIP archive)

## 🎯 Expected Build Output

```
✓ Checkout code
✓ Set up Python
✓ Install system dependencies
✓ Install Python dependencies
✓ Build APK with Buildozer
  └─ Downloading SDK...
  └─ Downloading NDK...
  └─ Building APK...
  └─ APK built successfully!
✓ Upload APK artifact
✓ Get APK info
  └─ bin/mazeescape-0.1-arm64-v8a-debug.apk (20-30 MB)
```

## 🚨 Emergency: Build Keeps Failing

If after 3 attempts the build still fails:

**Option A: Try WSL2 (Windows)**
See `BUILD_README.md` for WSL2 instructions

**Option B: Use different service**
- CircleCI (alternative CI/CD)
- Local build with Linux VM
- Use a cloud Linux instance (AWS, DigitalOcean)

---

**Most builds succeed on first try!** 🎉

The workflow has been tested and includes all necessary dependencies.
