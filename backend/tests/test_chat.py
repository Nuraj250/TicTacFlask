import unittest
from backend.app import app

class ChatTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_send_message(self):
        response = self.client.post('/api/chat/send-message', json={
            "match_id": 1,
            "sender_id": 1,
            "message": "Hello!"
        })
        self.assertEqual(response.status_code, 200)
