#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <ip-address>"
    exit 1
fi

TARGET=$1
OUTPUT="output/recon/nmap_${TARGET}.txt"

mkdir -p output/recon

echo "[*] Running Nmap scan on $TARGET..."
nmap -sS -T4 -A "$TARGET" -oN "$OUTPUT"

echo "[+] Scan complete. Results saved to $OUTPUT"
