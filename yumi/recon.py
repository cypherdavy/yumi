import requests
from bs4 import BeautifulSoup
import re

WAYBACK_API = "http://web.archive.org/cdx/search/cdx"

def enumerate_subdomains_and_js(domain):
    # Collect subdomains (basic + www)
    subdomains = [domain, f"www.{domain}"]

    js_urls = set()

    for sub in subdomains:
        for scheme in ["http://", "https://"]:
            url = f"{scheme}{sub}"
            try:
                resp = requests.get(url, timeout=8, headers={"User-Agent": "Yumi-Scanner"})
                if resp.status_code == 200:
                    js_urls.update(extract_js_links(resp.text, url))
            except Exception:
                continue

    # 🔥 Add JS from Wayback Machine
    js_urls.update(fetch_wayback_js(domain))

    return subdomains, list(js_urls)


def extract_js_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    js_urls = set()
    for script in soup.find_all("script", src=True):
        src = script["src"].strip()
        if src.startswith(("http://", "https://")):
            js_urls.add(src)
        elif src.startswith("//"):
            js_urls.add("https:" + src)
        elif src.startswith("/"):
            # normalize relative path
            base = base_url.rstrip("/")
            js_urls.add(base + src)
    return js_urls


def fetch_wayback_js(domain):
    """Fetch archived JS file URLs from Wayback Machine"""
    js_urls = set()
    try:
        params = {
            "url": f"*.{domain}/*.js",
            "output": "json",
            "fl": "original",
            "collapse": "urlkey"
        }
        resp = requests.get(WAYBACK_API, params=params, timeout=10)
        if resp.status_code == 200:
            data = resp.text.splitlines()
            for line in data[1:]:  # skip header
                parts = line.split(" ")
                if len(parts) > 0:
                    url = parts[0]
                    if url.endswith(".js"):
                        js_urls.add(url)
    except Exception:
        pass
    return js_urls
