from .custom_patterns import scan_content_for_custom_patterns

def run_plugins_scan(content):
    """
    Run all plugin scans on the provided content.
    """
    findings = []
    findings.extend(scan_content_for_custom_patterns(content))
    return findings
