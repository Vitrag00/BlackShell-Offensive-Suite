import sys

if len(sys.argv) < 2:
    print("Usage: python3 html_builder.py <target>")
    sys.exit(1)

target = sys.argv[1]
html = f"""
<html>
<head><title>Scan Report - {target}</title></head>
<body>
    <h1>BlackShell Scan Report</h1>
    <p><strong>Target:</strong> {target}</p>
    <ul>
        <li>Recon: Done</li>
        <li>VulnScan: XSS, SQLi suspected</li>
    </ul>
</body>
</html>
"""

with open(f"output/reports/{target}_report.html", "w") as f:
    f.write(html)

print(f"[+] HTML report saved to output/reports/{target}_report.html")
