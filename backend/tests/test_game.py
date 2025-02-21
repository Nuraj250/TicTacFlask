import unittest
from backend.app import app

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_play_move(self):
        response = self.client.post('/api/game/play_move', json={
            "match_id": 1,
            "game_data": [["X", "", ""], ["", "O", ""], ["", "", ""]]
        })
        self.assertEqual(response.status_code, 200)
