#!/bin/bash

echo "🔧 [BlackShell Setup Script]"

# Step 1: Create virtual environment
echo "[*] Creating Python virtual environment..."
python3 -m venv venv

# Step 2: Activate the venv
echo "[*] Activating virtual environment..."
source venv/bin/activate

# Step 3: Install Python dependencies
echo "[*] Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 4: Install Linux tools via apt
echo "[*] Installing Linux tools (nmap, whois, subfinder)..."
sudo apt update
sudo apt install -y nmap whois curl subfinder

# Step 5: Make shell scripts executable
echo "[*] Making shell scripts executable..."
find modules -type f -name "*.sh" -exec chmod +x {} \;

# Step 6: Create output directories
mkdir -p output/recon output/reports

echo "[✅] BlackShell environment setup complete!"
echo "[ℹ️] To activate your Python environment, run: source venv/bin/activate"
