import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestAPISecurity(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_vulnerable_bola_access(self):
        # Anyone can read Bob's document on the vulnerable endpoint
        resp = self.client.get("/api/v1/vulnerable/documents/doc_102")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Bob Private Vault", resp.json()["content"])

    def test_secure_bola_prevention(self):
        # Alice tries to read Bob's document on the secure endpoint
        headers = {"Authorization": "Bearer token_alice"}
        resp = self.client.get("/api/v1/secure/documents/doc_102", headers=headers)
        self.assertEqual(resp.status_code, 403)
        self.assertIn("Forbidden", resp.json()["detail"])

    def test_secure_legitimate_access(self):
        # Alice reads Alice's document
        headers = {"Authorization": "Bearer token_alice"}
        resp = self.client.get("/api/v1/secure/documents/doc_101", headers=headers)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["owner"], "user_alice")

if __name__ == "__main__":
    unittest.main()
