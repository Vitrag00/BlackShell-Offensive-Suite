import os

folders = [
    "BlackShell-Offensive-Suite/modules/recon",
    "BlackShell-Offensive-Suite/modules/scan",
    "BlackShell-Offensive-Suite/modules/vulnscan",
    "BlackShell-Offensive-Suite/modules/exploit/payloads",
    "BlackShell-Offensive-Suite/modules/report",
    "BlackShell-Offensive-Suite/utils",
    "BlackShell-Offensive-Suite/output/recon",
    "BlackShell-Offensive-Suite/output/reports"
]

files = [
    "BlackShell-Offensive-Suite/main.py",
    "BlackShell-Offensive-Suite/deploy.sh",
    "BlackShell-Offensive-Suite/requirements.txt",
    "BlackShell-Offensive-Suite/README.md",
    "BlackShell-Offensive-Suite/modules/recon/subfinder_wrapper.sh",
    "BlackShell-Offensive-Suite/modules/recon/whois_lookup.py",
    "BlackShell-Offensive-Suite/modules/recon/email_scraper.py",
    "BlackShell-Offensive-Suite/modules/recon/dns_enum.awk",
    "BlackShell-Offensive-Suite/modules/scan/nmap_wrapper.sh",
    "BlackShell-Offensive-Suite/modules/scan/port_filter.awk",
    "BlackShell-Offensive-Suite/modules/scan/vuln_summary_parser.py",
    "BlackShell-Offensive-Suite/modules/vulnscan/sql_injection_scanner.py",
    "BlackShell-Offensive-Suite/modules/vulnscan/xss_payload_generator.pl",
    "BlackShell-Offensive-Suite/modules/vulnscan/log4j_fuzzer.py",
    "BlackShell-Offensive-Suite/modules/exploit/lfi_exploit.py",
    "BlackShell-Offensive-Suite/modules/exploit/rce_launcher.sh",
    "BlackShell-Offensive-Suite/modules/exploit/payloads/shell_reverse_tcp.py",
    "BlackShell-Offensive-Suite/modules/report/markdown_report.py",
    "BlackShell-Offensive-Suite/modules/report/csv_export.sh",
    "BlackShell-Offensive-Suite/modules/report/html_builder.py",
    "BlackShell-Offensive-Suite/utils/banner.py",
    "BlackShell-Offensive-Suite/utils/log_handler.py",
    "BlackShell-Offensive-Suite/utils/config_loader.py"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        pass

print("✅ Folder and file structure created!")
