import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python3 sql_injection_scanner.py <url>")
    sys.exit(1)

url = sys.argv[1]
payload = "'"
target = url + payload

try:
    print(f"[*] Testing for SQL Injection at {target}")
    response = requests.get(target)
    if any(err in response.text.lower() for err in ["sql", "syntax", "mysql", "warning"]):
        print("[+] Possible SQL Injection vulnerability found!")
    else:
        print("[-] No obvious SQLi signs detected.")
except Exception as e:
    print(f"[!] Error: {e}")
