import unittest
from backend.app import app

class AITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_ai_move(self):
        response = self.client.post('/api/ai-move', json={
            "board": [["X", "", ""], ["", "O", ""], ["", "", ""]]
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("ai_move", response.get_json())
