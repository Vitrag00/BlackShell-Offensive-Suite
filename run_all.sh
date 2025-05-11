#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./run_all.sh <domain>"
    exit 1
fi

TARGET=$1

echo "🧠 [1] Recon: Subdomain Enumeration"
python main.py recon subfinder_wrapper.sh $TARGET

echo "🔍 [2] WHOIS Lookup"
python main.py recon whois_lookup.py $TARGET

echo "🔎 [3] Port Scan"
python main.py scan nmap_wrapper.sh $TARGET

echo "🚨 [4] Vuln Scan (SQLi)"
python main.py vulnscan sql_injection_scanner.py http://$TARGET/page.php?id=1

echo "📊 [5] Generate Markdown Report"
python main.py report markdown_report.py $TARGET

echo "📁 All output saved to output/ folder"
