# Building APK with GitHub Actions (Cloud Build)

This is the **EASIEST** way to build your APK without setting up any local build environment!

## Prerequisites

- A GitHub account (free)
- Git installed on your computer

## Steps

### 1. Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **+** icon in the top right corner
3. Select **New repository**
4. Name it (e.g., "maze-escape-game")
5. Choose **Public** or **Private**
6. Click **Create repository**

### 2. Push Your Code to GitHub

Open PowerShell in your project directory and run:

```powershell
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit - Maze Escape Game"

# Add GitHub as remote (replace YOUR_USERNAME and YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git push -u origin master
```

**Note:** If you get an error about `master` vs `main`, use `main` instead:
```powershell
git branch -M main
git push -u origin main
```

### 3. Trigger the Build

Once your code is pushed:

1. Go to your repository on GitHub
2. Click on the **Actions** tab
3. You should see a workflow run starting automatically
4. If not, click **"Build Android APK"** on the left
5. Click **"Run workflow"** button on the right
6. Click the green **"Run workflow"** button

### 4. Wait for Build to Complete

- The build takes about **20-30 minutes** on the first run
- You can watch the progress in real-time
- ☑️ Green checkmark = Success!
- ❌ Red X = Failed (check the logs)

### 5. Download Your APK

After the build completes:

1. Click on the completed workflow run
2. Scroll down to **"Artifacts"** section
3. Click **"maze-escape-apk"** to download
4. Extract the ZIP file
5. You'll find your APK inside!

### 6. Install on Android Device

1. Transfer the APK to your Android device
2. Enable **"Install from Unknown Sources"**
3. Tap the APK file to install

## Troubleshooting

### "git: command not found"

Install Git:
- Windows: Download from [git-scm.com](https://git-scm.com/)
- Or use GitHub Desktop: [desktop.github.com](https://desktop.github.com/)

### Authentication Issues

GitHub now requires a Personal Access Token instead of password:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name (e.g., "maze-game-upload")
4. Check the **"repo"** scope
5. Click "Generate token"
6. Copy the token and use it as your password when pushing

### Build Fails

Check the GitHub Actions logs:
1. Click on the failed workflow run
2. Click on the "build" job
3. Expand each step to see error messages
4. Common issues:
   - Missing dependencies (usually auto-fixed by workflow)
   - buildozer.spec errors (check your file)

## Alternative: Using GitHub Desktop (GUI)

If you prefer a graphical interface:

1. Download [GitHub Desktop](https://desktop.github.com/)
2. Install and sign in
3. Click **"Add"** → **"Add existing repository"**
4. Select your maze game folder
5. Click **"Publish repository"** button
6. Follow steps 3-6 above

## Advantages of GitHub Actions

✅ No local setup required  
✅ Works on any operating system  
✅ Free for public repositories  
✅ Automatic builds on every commit  
✅ Professional CI/CD workflow  
✅ Can build for multiple architectures  

## Build Configuration

The build configuration is in `.github/workflows/build-apk.yml`

You can modify it to:
- Build on different triggers (tags, releases, etc.)
- Build release APKs (with signing)
- Run tests before building
- Deploy to Google Play Store automatically

## Next Steps

After building your first APK successfully, you might want to:

1. **Add a release build** with signing keys
2. **Set up automated versioning**
3. **Add automated testing**
4. **Configure Google Play Store deployment**

See the main BUILD_README.md for more advanced options!

---

**Happy Building! 🚀**
