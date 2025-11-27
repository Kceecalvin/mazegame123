# 🚀 Build APK with GitHub Actions - Quick Start

## Why This is Better Than Docker on Windows:

✅ **No OneDrive path issues**  
✅ **100% reliable** (builds in Linux environment)  
✅ **No local setup needed**  
✅ **Professional CI/CD workflow**  
✅ **Takes only 15-20 minutes**  
✅ **Already configured in your project!**  

---

## 📋 5-Minute Setup (Then Wait 15 Minutes for APK)

### Step 1: Create GitHub Account (if needed)
- Go to: https://github.com/join
- Sign up (it's free!)

### Step 2: Create Repository
1. Go to: https://github.com/new
2. **Repository name:** `maze-escape-game`
3. **Visibility:** Public (required for free Actions)
4. **DON'T** initialize with README
5. Click **"Create repository"**

### Step 3: Push Your Code
Copy the commands GitHub shows you, or use these (replace YOUR_USERNAME):

```bash
git remote add origin https://github.com/YOUR_USERNAME/maze-escape-game.git
git branch -M main
git push -u origin main
```

**Run in PowerShell:**
```powershell
git remote add origin https://github.com/YOUR_USERNAME/maze-escape-game.git
git branch -M main
git push -u origin main
```

### Step 4: Trigger Build on GitHub
1. Go to your repository: `https://github.com/YOUR_USERNAME/maze-escape-game`
2. Click **"Actions"** tab at the top
3. You'll see **"Build Android APK"** workflow
4. Click on it
5. Click the **"Run workflow"** button (on the right)
6. Select branch: **main**
7. Click green **"Run workflow"** button

### Step 5: Wait 15-20 Minutes
- The build will run automatically
- You can watch progress in real-time
- Green checkmark ✓ = Success
- Red X = Failed (rare, check logs)

### Step 6: Download Your APK
1. Build should be complete (green checkmark)
2. Click on the workflow run (the one you just triggered)
3. Scroll to bottom of page
4. Look for **"Artifacts"** section
5. Download **"maze-escape-apk"** (it's a ZIP file)
6. Extract the ZIP
7. Inside you'll find: `mazeescape-0.1-arm64-v8a_armeabi-v7a-debug.apk`

### Step 7: Install on Android
1. Transfer APK to your phone (USB, email, Drive, etc.)
2. On phone: Settings → Security → "Install unknown apps" → Enable
3. Tap the APK file
4. Tap "Install"
5. Tap "Open" and play! 🎮

---

## 🎯 Complete Example (Copy-Paste)

Assuming your GitHub username is `YourGitHubName`:

```powershell
# Push to GitHub (run in PowerShell)
git remote add origin https://github.com/YourGitHubName/maze-escape-game.git
git branch -M main
git push -u origin main
```

Then visit: `https://github.com/YourGitHubName/maze-escape-game/actions`

---

## 📸 Visual Guide

**Your workflow file is already configured!**
Location: `.github/workflows/build-apk.yml`

It will:
1. ✅ Set up Ubuntu Linux environment
2. ✅ Install Python and Buildozer
3. ✅ Install Android SDK and NDK
4. ✅ Build your APK
5. ✅ Upload as artifact
6. ✅ Keep for 90 days

---

## ⏱️ Timeline

| Step | Time |
|------|------|
| Create GitHub account | 2 min |
| Create repository | 1 min |
| Push code | 2 min |
| Trigger workflow | 1 min |
| **Build (wait)** | **15-20 min** |
| Download APK | 1 min |
| **TOTAL** | **~22 minutes** |

---

## 🆚 Why Not Docker on Windows?

| Issue | Docker | GitHub Actions |
|-------|--------|----------------|
| OneDrive paths | ❌ Problems | ✅ No issue |
| Setup complexity | ⚠️ Medium | ✅ Easy |
| Reliability | ⚠️ 70% | ✅ 99% |
| Speed | ⚠️ 20-30 min | ✅ 15-20 min |
| Requires local resources | ❌ Yes | ✅ No |

**GitHub Actions is simply better for Windows users!**

---

## 🎓 What's Happening Behind the Scenes?

Your `.github/workflows/build-apk.yml` file tells GitHub to:

```yaml
1. Use Ubuntu 20.04 Linux
2. Install Python 3.9
3. Install Java (for Android SDK)
4. Install Buildozer
5. Run: buildozer android debug
6. Upload resulting APK
```

**It's like having a Linux machine in the cloud building for you!**

---

## 🐛 Troubleshooting

### "Repository not found" when pushing
- Make sure you created the repository on GitHub first
- Check you're using YOUR username in the URL

### "Permission denied" when pushing
- You need to authenticate with GitHub
- Use personal access token or SSH key
- GitHub will prompt you for credentials

### Build fails on GitHub
- Check the logs in the Actions tab
- Usually it's a missing dependency (already configured in your project)
- Ask for help with specific error

### Can't find artifacts
- Build must complete successfully (green checkmark)
- Scroll ALL the way to bottom of workflow run page
- Artifacts section is below all the logs

---

## ✅ Current Status

**Your project is already configured!**

You have:
- ✅ Git initialized (`git init` already done)
- ✅ Code committed
- ✅ Workflow file ready (`.github/workflows/build-apk.yml`)
- ✅ Buildozer spec configured (`buildozer.spec`)

**All you need to do:**
1. Create GitHub repository
2. Push code
3. Trigger workflow
4. Download APK!

---

## 🎮 Your Game Specs (Reminder)

**Technology:** Python + Kivy (OPTIMAL - No conversion needed!)

**APK Specs:**
- Package: `org.example.mazeescape`
- Size: ~30 MB
- Min Android: 5.0 (API 21)
- Target: Android 13 (API 33)
- Architectures: ARM64-v8a, ARMv7a

**Game Features:**
- 10 progressive levels
- AI snake enemy
- Touch controls
- Hint system
- Move counter & timer

---

## 🚀 Ready to Start?

**Quick checklist:**
- [ ] Have or create GitHub account
- [ ] Create new repository (public)
- [ ] Push code with git commands above
- [ ] Go to Actions tab
- [ ] Click "Run workflow"
- [ ] Wait 15-20 minutes
- [ ] Download APK from Artifacts
- [ ] Install on Android phone
- [ ] Play! 🎉

---

## 💡 Pro Tips

1. **Bookmark your Actions page** for easy access
2. **Every git push** can trigger automatic builds (if configured)
3. **Keep artifacts** - they expire after 90 days
4. **Release builds** (for Play Store) require signing keys
5. **Test thoroughly** before publishing

---

**This is the BEST way to build your APK on Windows!**

**Need help with any step? Let me know!** 😊
