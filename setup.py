from setuptools import setup, find_packages

setup(
    name="yumi",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "rich",
        "pyfiglet"
    ],
    entry_points={
        "console_scripts": [
            "yumi = yumi.main:main"
        ],
    },
    author="Your Name",
    description="Yumi - JS Recon & P1 Bug Hunter",
    url="https://github.com/yourgithub/yumi"
)
from yumi.plugins import run_plugins_scan

def scan_js_content(url, content):
    findings = []


    plugin_findings = run_plugins_scan(content)

    for f in plugin_findings:
        f['url'] = url
    findings.extend(plugin_findings)

    return findings

