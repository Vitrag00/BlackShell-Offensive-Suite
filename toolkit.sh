#!/bin/bash

# Color variables for styling
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
banner() {
    clear
    echo -e "${BLUE}"
    echo "==========================================="
    echo "    ⚔️  Ethical Hacking Tool Interface ⚔️   "
    echo "==========================================="
    echo -e "${NC}"
}

# Menu
show_menu() {
    echo -e "${YELLOW}Select an option:${NC}"
    echo "1. Run SQL Injection Scanner"
    echo "2. Run XSS Payload Tester"
    echo "3. Whois Lookup"
    echo "4. Nmap Quick Scan"
    echo "5. Exit"
}

# Actions
sql_injection_scanner() {
    read -p "Enter target URL (e.g., http://example.com/page?id=1): " url
    python3 sql_injection_scanner.py "$url"
}

xss_payload_tester() {
    read -p "Enter target URL: " target
    echo "<script>alert(1)</script>" >> payload.txt
    curl -s -X GET "$target?search=<script>alert(1)</script>" > xss_output.txt
    echo -e "${GREEN}[+] XSS test sent to $target. Check xss_output.txt for response.${NC}"
}

whois_lookup() {
    read -p "Enter domain name: " domain
    whois "$domain"
}

nmap_scan() {
    read -p "Enter IP or domain: " target
    nmap -T4 -F "$target"
}

# Main Loop
while true; do
    banner
    show_menu
    read -p ">> Enter choice [1-5]: " choice
    case $choice in
        1) sql_injection_scanner ;;
        2) xss_payload_tester ;;
        3) whois_lookup ;;
        4) nmap_scan ;;
        5) echo -e "${RED}Exiting...${NC}"; break ;;
        *) echo -e "${RED}Invalid choice. Try again.${NC}" ;;
    esac
    read -p "Press Enter to return to menu..."
done
