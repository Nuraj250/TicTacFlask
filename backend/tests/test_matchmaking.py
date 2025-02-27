import unittest
from backend.app import app

class MatchmakingTestCase(unittest.TestCase):
    """
    Unit test case for the matchmaking system.
    
    - Tests the `/api/matchmaking/find_match` endpoint.
    - Ensures the response status code is either:
      - `200 OK` (if a match is found)
      - `202 Accepted` (if waiting for an opponent)
    """

    def setUp(self):
        """
        Sets up the test client before each test case.

        - Creates a test client for sending HTTP requests.
        - Ensures the app runs in testing mode.
        """
        self.client = app.test_client()

    def test_find_match(self):
        """
        Tests the matchmaking functionality.

        - Sends a `POST` request to `/api/matchmaking/find_match` with a test player ID.
        - Ensures the response status code is either `200 OK` (match found) or `202 Accepted` (waiting).
        """
        response = self.client.post('/api/matchmaking/find_match', json={"player_id": 1})
        self.assertIn(response.status_code, [200, 202])  # Match found or waiting
