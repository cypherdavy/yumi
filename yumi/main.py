import subprocess

def collect_js_files(target):
    js_urls = set()
    try:
        # waybackurls
        wb = subprocess.check_output(["waybackurls", target], text=True, stderr=subprocess.DEVNULL)
        js_urls.update([u for u in wb.splitlines() if u.endswith(".js")])
    except:
        pass

    try:
        # gau
        ga = subprocess.check_output(["gau", target], text=True, stderr=subprocess.DEVNULL)
        js_urls.update([u for u in ga.splitlines() if ".js" in u])
    except:
        pass

    return sorted(js_urls)
