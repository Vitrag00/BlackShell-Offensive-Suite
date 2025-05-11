#!/bin/bash

# Check if target domain is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

DOMAIN=$1
OUTPUT_DIR="output/recon"
OUTPUT_FILE="${OUTPUT_DIR}/${DOMAIN}_subdomains.txt"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "[*] Running subfinder on $DOMAIN..."
subfinder -d "$DOMAIN" -silent | tee "$OUTPUT_FILE"

echo "[+] Subdomains saved to $OUTPUT_FILE"
