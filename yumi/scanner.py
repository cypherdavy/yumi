
import re

# Simple regex patterns to detect API keys, tokens, etc.
PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Google API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "JWT Token": r"eyJ[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.[A-Za-z0-9-_.+/=]*",
    "Hardcoded Password": r"password\s*=\s*[\"'].*?[\"']",
}

def scan_js_content(url, content):
    findings = []
    for name, pattern in PATTERNS.items():
        matches = re.findall(pattern, content)
        if matches:
            for match in matches:
                findings.append({
                    "url": url,
                    "type": name,
                    "match": match
                })
    return findings
