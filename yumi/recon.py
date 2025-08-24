import requests
from bs4 import BeautifulSoup
import re

def enumerate_subdomains_and_js(domain):
    # For demo: naive subdomain gathering: main domain + www
    subdomains = [domain, f"www.{domain}"]

    js_urls = set()

    for sub in subdomains:
        url = f"http://{sub}"
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200:
                js_urls.update(extract_js_links(resp.text, url))
        except Exception:
            continue

    return subdomains, list(js_urls)

def extract_js_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    js_urls = set()
    for script in soup.find_all("script", src=True):
        src = script['src']
        if src.startswith(("http://", "https://")):
            js_urls.add(src)
        elif src.startswith("/"):
            js_urls.add(base_url.rstrip("/") + src)
    return js_urls

