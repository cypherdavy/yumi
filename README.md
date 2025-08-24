
# Yumi

![Version](https://img.shields.io/badge/version-0.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Yumi is a terminal-based JavaScript reconnaissance and P1 bug bounty hunting tool that automatically collects JavaScript files from a domain and its subdomains, scans for sensitive information, and helps bug bounty hunters find critical security vulnerabilities with ease.

---

## Features

- Automatic enumeration of subdomains and JavaScript files
- Bulk download and scanning of JS files for sensitive keys, secrets, and endpoints
- Detects common P1 bug bounty vulnerabilities such as API keys, tokens, hardcoded passwords, and more
- Fancy terminal UI with ASCII art logo and loading animations
- JSON and console report generation
- Extensible plugin system for custom scanning rules

---

## Installation

Ensure you have Python 3.8+ installed, then run:

```
pip install -r requirements.txt
```

Or install in editable mode for development:

```
pip install -e .
```

---

## Usage

Run the tool from the command line with a target domain:

```
yumi example.com
```

You will see a colorful loading screen, followed by enumeration and scan results. A detailed JSON report is saved as `report.json`.

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues](https://github.com/yourgithub/yumi/issues) page.

To contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Authors and Acknowledgments

- Developed and maintained by Your Name  
- Inspired by the needs of the bug bounty community  
- Thanks to open source projects like `requests`, `rich`, and `pyfiglet`

---

## Contact


GitHub: [https://github.com/cypherdavy/yumi](https://github.com/cypherdavy/yumi)
