[app]

# (str) Title of your application
title = FaceApp

# (str) Package name
package.name = com.archtech.faceapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivy

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,json,xml,spec

# (list) Application version
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,opencv-python,pandas,requests,fpdf,apscheduler,edge-tts,pygame,kivy-garden.androidstorage

# (str) The Android archs to build for.
android.archs = arm64-v8a, armeabi-v7a

# (str) Python interpreter version to use
android.python = 3.11

# (list) Android permissions to request
android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API version
android.api = 33

# (int) Minimum Android API version
android.minapi = 21

# (int) The version code for the Android app
android.version_code = 1

# (str) The file name of the app icon
icon.filename = icon.png

# (list) Your app's assets. Note: We are no longer including the haarcascade file here, as it's downloaded at runtime.
android.add_assets = 

[buildozer]

# (list) Buildozer specific requirements
# (str) The build platform
# (str) The build host
# (str) The build directory
# (str) The install directory
# (str) The temporary directory
# (str) The path to the buildozer log file
# (bool) Log to stdout?
# (int) Log level
