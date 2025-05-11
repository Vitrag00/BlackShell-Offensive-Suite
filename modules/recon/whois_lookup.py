import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3 whois_lookup.py <domain>")
    sys.exit(1)

domain = sys.argv[1]
os.system(f"whois {domain}")
