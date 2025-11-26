#!/bin/bash
# Build APK using WSL2 Ubuntu and Buildozer

echo "================================"
echo "Building Maze Escape APK in WSL2"
echo "================================"
echo ""

# Install buildozer if not present
if ! command -v buildozer &> /dev/null; then
    echo "Installing Buildozer..."
    sudo apt-get update
    sudo apt-get install -y python3-pip python3-venv git zip unzip openjdk-11-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev cmake ccache
    pip3 install --user --upgrade buildozer cython==0.29.33
    export PATH=$PATH:~/.local/bin
fi

echo "Starting APK build..."
echo ""

buildozer android debug

if [ $? -eq 0 ]; then
    echo ""
    echo "================================"
    echo "BUILD SUCCESSFUL!"
    echo "================================"
    echo ""
    echo "APK Location:"
    ls -lh bin/*.apk
else
    echo ""
    echo "================================"
    echo "BUILD FAILED!"
    echo "================================"
fi
