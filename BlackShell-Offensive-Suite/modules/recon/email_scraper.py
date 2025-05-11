import re
import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python3 email_scraper.py <url>")
    sys.exit(1)

url = sys.argv[1]
r = requests.get(url)
emails = set(re.findall(r"[\w\.-]+@[\w\.-]+", r.text))

print(f"[+] Found {len(emails)} emails:")
for email in emails:
    print(email)
