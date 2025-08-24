import unittest
from yumi import ui

class TestUI(unittest.TestCase):
    def test_display_logo_and_loading_runs(self):
        # As this just prints, test that it runs without error
        try:
            ui.display_logo_and_loading()
        except Exception as e:
            self.fail(f"display_logo_and_loading() raised Exception: {e}")

if __name__ == "__main__":
    unittest.main()


