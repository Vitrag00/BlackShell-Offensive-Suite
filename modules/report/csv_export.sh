#!/bin/bash

TARGET=$1
OUT="output/reports/${TARGET}_scan.csv"

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

mkdir -p output/reports
echo "scan_type,result" > "$OUT"
echo "nmap,success" >> "$OUT"
echo "vulnscan,partial" >> "$OUT"

echo "[+] CSV report saved to $OUT"
