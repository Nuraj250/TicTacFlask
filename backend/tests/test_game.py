import unittest
from backend.app import app

class GameTestCase(unittest.TestCase):
    """
    Unit test case for the game move API.
    
    - Tests the `/api/game/play_move` endpoint.
    - Ensures the response status code is `200 OK` if the move is successfully recorded.
    """

    def setUp(self):
        """
        Sets up the test client before each test case.

        - Creates a test client for sending HTTP requests.
        - Ensures the app runs in testing mode.
        """
        self.client = app.test_client()

    def test_play_move(self):
        """
        Tests the move-playing functionality.

        - Sends a `POST` request to `/api/game/play_move` with a test match ID and board state.
        - Ensures the response status code is `200 OK` if the move is valid.
        """
        response = self.client.post('/api/game/play_move', json={
            "match_id": 1,
            "game_data": [["X", "", ""], ["", "O", ""], ["", "", ""]]
        })
        self.assertEqual(response.status_code, 200)  # Move should be accepted
