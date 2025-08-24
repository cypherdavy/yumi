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
    author="Davy Cipher",
    description="Yumi - JS Recon & P1 Bug Hunter",
    url="https://github.com/cypherdavy/yumi"
)
