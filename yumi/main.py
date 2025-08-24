import subprocess

def run_cmd(cmd):
    try:
        out = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL)
        return out.splitlines()
    except subprocess.CalledProcessError:
        return []

def enumerate_subdomains_and_js(domain):
    subdomains = set()
    js_urls = set()

    # collect subdomains (subfinder / assetfinder / amass if installed)
    subdomains.update(run_cmd(f"subfinder -silent -d {domain}"))
    subdomains.update(run_cmd(f"assetfinder --subs-only {domain}"))

    # collect JS URLs from different sources
    js_urls.update(u for u in run_cmd(f"waybackurls {domain}") if ".js" in u)
    js_urls.update(u for u in run_cmd(f"gau {domain}") if ".js" in u)
    js_urls.update(u for u in run_cmd(f"katana -u https://{domain} -em js -d 2 -silent") if ".js" in u)

    return list(subdomains), list(js_urls)
