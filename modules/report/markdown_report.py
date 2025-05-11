def generate_report(target):
    content = f"# BlackShell Report for {target}\n\n"
    content += "- Scan: ✅ Done\n"
    content += "- Vulnerabilities: Potential XSS, SQLi, LFI\n"
    content += "- Subdomains: Check output/recon\n"

    with open(f"output/reports/{target}_report.md", "w") as f:
        f.write(content)

    print(f"[+] Markdown report saved to output/reports/{target}_report.md")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 markdown_report.py <target>")
    else:
        generate_report(sys.argv[1])
