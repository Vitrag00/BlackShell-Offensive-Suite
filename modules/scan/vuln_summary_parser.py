import sys

if len(sys.argv) < 2:
    print("Usage: python3 vuln_summary_parser.py <nmap_output_file>")
    sys.exit(1)

filepath = sys.argv[1]

print(f"[+] Extracting possible vulnerabilities from {filepath}\n")
with open(filepath, 'r') as f:
    for line in f:
        if 'vuln' in line.lower() or 'cve' in line.lower():
            print(line.strip())
