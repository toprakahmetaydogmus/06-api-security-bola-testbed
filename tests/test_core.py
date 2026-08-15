import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestAPIBOLA(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_vulnerable_endpoint(self):
        res = self.client.get("/api/v1/vulnerable/documents/doc_102")
        self.assertEqual(res.status_code, 200)

    def test_secure_endpoint_unauthorized(self):
        headers = {"Authorization": "Bearer token_alice"}
        res = self.client.get("/api/v1/secure/documents/doc_102", headers=headers)
        self.assertEqual(res.status_code, 403)

if __name__ == "__main__":
    unittest.main()
