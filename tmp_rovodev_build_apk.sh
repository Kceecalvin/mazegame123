#!/bin/bash
# Bash script to build APK for Maze Escape Game
# This script sets up the environment and builds the Android APK using Buildozer

echo "=== Maze Escape APK Builder ==="
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo -e "${YELLOW}Warning: macOS detected. Buildozer for Android works best on Linux.${NC}"
        echo "For iOS builds, use different tools. For Android, consider using a Linux VM or WSL."
    fi
fi

echo -e "${CYAN}Step 1: Installing system dependencies...${NC}"
echo "This will install required packages using apt (requires sudo)"
echo ""

# Update package list
sudo apt-get update

# Install Python and build essentials
sudo apt-get install -y python3 python3-pip python3-venv git \
    build-essential libssl-dev libffi-dev \
    libpython3-dev python3-setuptools

# Install buildozer dependencies
sudo apt-get install -y zip unzip openjdk-11-jdk autoconf libtool \
    pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev \
    libtinfo5 cmake libffi-dev libssl-dev

# Install Cython
pip3 install --upgrade pip
pip3 install --upgrade cython==0.29.33

echo ""
echo -e "${CYAN}Step 2: Installing Buildozer...${NC}"
pip3 install --upgrade buildozer

echo ""
echo -e "${CYAN}Step 3: Initializing Buildozer (if needed)...${NC}"
# The buildozer.spec already exists, so we'll use it

echo ""
echo -e "${CYAN}Step 4: Cleaning previous builds...${NC}"
buildozer android clean || true

echo ""
echo -e "${GREEN}Step 5: Building APK... (This may take 15-30 minutes on first build)${NC}"
echo "Buildozer will download Android SDK, NDK, and other dependencies automatically."
echo ""

# Build the APK
buildozer -v android debug

# Check if build was successful
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}SUCCESS! APK has been built!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo -e "APK Location: ${CYAN}bin/mazeescape-0.1-arm64-v8a-debug.apk${NC}"
    echo ""
    echo "To install on your Android device:"
    echo "1. Enable 'Unknown Sources' in Android Settings > Security"
    echo "2. Transfer the APK to your device"
    echo "3. Open the APK file on your device to install"
    echo ""
    echo "Or use ADB:"
    echo "  adb install bin/mazeescape-0.1-arm64-v8a-debug.apk"
    echo ""
else
    echo ""
    echo -e "${RED}========================================${NC}"
    echo -e "${RED}BUILD FAILED!${NC}"
    echo -e "${RED}========================================${NC}"
    echo ""
    echo "Check the error messages above for details."
    echo "Common issues:"
    echo "1. Missing dependencies - run the apt-get commands again"
    echo "2. Java version issues - ensure Java 11 is installed"
    echo "3. Network issues - buildozer needs to download dependencies"
    echo ""
    exit 1
fi
