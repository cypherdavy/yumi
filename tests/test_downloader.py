import unittest
from yumi import downloader

class TestDownloader(unittest.TestCase):
    def test_download_js_files(self):
        urls = [
            "https://code.jquery.com/jquery-3.6.0.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.6/umd/popper.min.js"
        ]
        contents = downloader.download_js_files(urls)
        self.assertIsInstance(contents, dict)
        self.assertTrue(all(url in contents for url in urls))

if __name__ == "__main__":
    unittest.main()

