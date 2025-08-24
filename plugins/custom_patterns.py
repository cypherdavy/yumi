import re

CUSTOM_PATTERNS = {
    "Slack Token": r"xox[baprs]-[0-9a-zA-Z]{10,48}",
    "Stripe Secret Key": r"sk_live_[0-9a-zA-Z]{24}",
    "Private RSA Key": r"-----BEGIN PRIVATE KEY-----[\s\S]+?-----END PRIVATE KEY-----",
}

def scan_content_for_custom_patterns(content):
    findings = []
    for name, pattern in CUSTOM_PATTERNS.items():
        matches = re.findall(pattern, content)
        for match in matches:
            findings.append({
                "type": name,
                "match": match
            })
    return findings
