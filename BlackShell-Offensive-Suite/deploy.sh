#!/bin/bash

echo "[*] Setting up BlackShell Environment..."
sudo apt update
sudo apt install -y python3 python3-pip subfinder nmap curl whois git
pip3 install -r requirements.txt
chmod +x modules/**/*.sh
mkdir -p output/recon output/reports
echo "[+] Setup complete."
