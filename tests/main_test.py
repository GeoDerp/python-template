import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from python_template.main import app


class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_request_success(self):
        # Mock test, if request was successful and html was passed
        with (
            patch("os.path.isfile", return_value=True),
            patch("builtins.open") as mock_open,
        ):
            mock_open.return_value.__enter__.return_value.read.return_value = (
                "<html><body>Hello, World!</body></html>"
            )
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.text, "<html><body>Hello, World!</body></html>")

    def test_file_not_found(self):
        # Test if file is not found
        with patch("os.path.isfile", return_value=False):
            response = self.client.get("/")
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json(), {"detail": "HTML template not found"})


if __name__ == "__main__":
    unittest.main()
