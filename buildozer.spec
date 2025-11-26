[app]
# (str) Title of your application
title = Maze Escape

# (str) Package name
package.name = mazeescape

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.2.1,numpy

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,VIBRATE,WAKE_LOCK

# (bool) Android wakelock to prevent screen from sleeping
android.wakelock = True

# (str) Presplash background color (for splash screen)
android.presplash_color = #4169E1

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then automatically accept SDK license agreements. This is intended for automation only.
android.accept_sdk_license = True

# (str) python-for-android (p4a) fork to use (if empty, will use official)
# p4a.fork = kivy

# (str) python-for-android branch to use (if empty, will use master)
p4a.branch = master

# (str) The bootstrap to use. Leave empty to let buildozer choose.
p4a.bootstrap = sdl2

# (int) Android API to use with python-for-android
p4a.android_api = 31

# (int) Minimum API for python-for-android
p4a.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a,armeabi-v7a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1