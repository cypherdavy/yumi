import argparse
from yumi.ui import display_logo_and_loading
from yumi.recon import enumerate_subdomains_and_js
from yumi.downloader import download_js_files
from yumi.scanner import scan_js_content
from yumi.report import generate_report

def main():
    display_logo_and_loading()

    parser = argparse.ArgumentParser(description="Yumi - JS Recon & P1 Bug Hunter")
    parser.add_argument("domain", help="Domain to scan (e.g. example.com)")
    args = parser.parse_args()

    domain = args.domain
    print(f"[+] Starting recon on {domain}")

    subdomains, js_urls = enumerate_subdomains_and_js(domain)
    print(f"[+] Found {len(subdomains)} subdomains and {len(js_urls)} JS files")

    js_contents = download_js_files(js_urls)
    print(f"[+] Downloaded {len(js_contents)} JS files")

    findings = []
    for url, content in js_contents.items():
        findings += scan_js_content(url, content)

    generate_report(findings)
    print("[+] Scan complete.")
