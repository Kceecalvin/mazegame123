#!/bin/bash
# Bash script to build APK using Docker

echo "=== Maze Escape Docker APK Builder ==="
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${RED}[ERROR] Docker is not installed!${NC}"
    echo ""
    echo "Please install Docker:"
    echo "  Ubuntu/Debian: sudo apt-get install docker.io"
    echo "  Or visit: https://docs.docker.com/get-docker/"
    exit 1
fi

echo -e "${GREEN}[OK] Docker is installed${NC}"

# Check if Docker is running
if ! docker ps &> /dev/null; then
    echo -e "${RED}[ERROR] Docker is not running!${NC}"
    echo "Please start Docker and try again."
    echo "  sudo systemctl start docker"
    exit 1
fi

echo -e "${GREEN}[OK] Docker is running${NC}"
echo ""

echo -e "${CYAN}Building Docker image...${NC}"
docker build -t maze-escape-builder .

if [ $? -ne 0 ]; then
    echo ""
    echo -e "${RED}[ERROR] Docker image build failed!${NC}"
    exit 1
fi

echo ""
echo -e "${CYAN}Building APK with Docker...${NC}"
echo -e "${YELLOW}This will take 20-30 minutes on first build...${NC}"
echo ""

# Run the build in Docker container
docker run --rm -v "$(pwd):/app" maze-escape-builder

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}SUCCESS! APK has been built!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo -e "APK Location: ${CYAN}bin/mazeescape-0.1-arm64-v8a-debug.apk${NC}"
    echo ""
else
    echo ""
    echo -e "${RED}========================================${NC}"
    echo -e "${RED}BUILD FAILED!${NC}"
    echo -e "${RED}========================================${NC}"
    echo ""
    exit 1
fi
