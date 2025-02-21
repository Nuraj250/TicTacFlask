import unittest
from backend.app import app

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_register_user(self):
        response = self.client.post('/api/auth/register', json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        self.client.post('/api/auth/register', json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        })
        response = self.client.post('/api/auth/login', json={
            "email": "test@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 200)
