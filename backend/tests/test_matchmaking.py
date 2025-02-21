import unittest
from backend.app import app

class MatchmakingTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_find_match(self):
        response = self.client.post('/api/matchmaking/find_match', json={"player_id": 1})
        self.assertIn(response.status_code, [200, 202])
