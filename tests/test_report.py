import unittest
import os
from yumi import report

class TestReport(unittest.TestCase):
    def test_generate_report_creates_file(self):
        findings = [
            {"url": "https://example.com/script.js", "type": "Hardcoded Password", "match": "password = \"1234\""}
        ]
        report.generate_report(findings)
        self.assertTrue(os.path.exists("report.json"))
        os.remove("report.json")

if __name__ == "__main__":
    unittest.main()

