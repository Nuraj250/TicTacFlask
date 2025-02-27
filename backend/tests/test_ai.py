import unittest
from backend.app import app

class AITestCase(unittest.TestCase):
    """
    Unit test case for AI move generation.

    - Tests the `/api/ai-move` endpoint.
    - Ensures AI returns a valid move based on the given board state.
    """

    def setUp(self):
        """
        Sets up the test client before each test case.

        - Creates a test client for sending HTTP requests.
        - Ensures the app runs in testing mode.
        """
        self.client = app.test_client()

    def test_ai_move(self):
        """
        Tests the AI move generation functionality.

        - Sends a `POST` request to `/api/ai-move` with a test board state.
        - Ensures the response status code is `200 OK`.
        - Ensures the response contains an `"ai_move"` key.
        """
        response = self.client.post('/api/ai-move', json={
            "board": [["X", "", ""], ["", "O", ""], ["", "", ""]]
        })

        # Check if the request was successful
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the AI move
        data = response.get_json()
        self.assertIn("ai_move", data)
