import requests

def download_js_files(urls):
    js_contents = {}
    for url in urls:
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                js_contents[url] = resp.text
        except Exception:
            continue
    return js_contents

