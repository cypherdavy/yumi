import unittest
from yumi import recon

class TestRecon(unittest.TestCase):
    def test_extract_js_links(self):
        html = '''
        <html>
          <head>
            <script src="https://example.com/script1.js"></script>
            <script src="/script2.js"></script>
          </head>
        </html>'''
        base_url = "https://example.com"
        js_links = recon.extract_js_links(html, base_url)
        self.assertIn("https://example.com/script1.js", js_links)
        self.assertIn("https://example.com/script2.js", js_links)

    def test_enumerate_subdomains_and_js(self):
        domain = "example.com"
        subs, js_urls = recon.enumerate_subdomains_and_js(domain)
        # Just test the return types for this basic test
        self.assertIsInstance(subs, list)
        self.assertIsInstance(js_urls, list)

if __name__ == "__main__":
    unittest.main()

