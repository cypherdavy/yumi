import unittest
from yumi import scanner

class TestScanner(unittest.TestCase):
    def test_scan_js_content(self):
        js = '''
        const apiKey = "AIzaSyD9gfExampleKey12345";
        const password = "supersecret123";
        '''
        results = scanner.scan_js_content("https://example.com/test.js", js)
        self.assertTrue(any(f['type'] == "Google API Key" for f in results))
        self.assertTrue(any(f['type'] == "Hardcoded Password" for f in results))

if __name__ == "__main__":
    unittest.main()

