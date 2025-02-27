import unittest
from backend.app import app

class ChatTestCase(unittest.TestCase):
    """
    Unit test case for the chat messaging API.

    - Tests the `/api/chat/send-message` endpoint.
    - Ensures the response status code is `200 OK` when a message is sent successfully.
    """

    def setUp(self):
        """
        Sets up the test client before each test case.

        - Creates a test client for sending HTTP requests.
        - Ensures the app runs in testing mode.
        """
        self.client = app.test_client()

    def test_send_message(self):
        """
        Tests the chat message functionality.

        - Sends a `POST` request to `/api/chat/send-message` with match ID, sender ID, and message.
        - Ensures the response status code is `200 OK` if the message is sent successfully.
        """
        response = self.client.post('/api/chat/send-message', json={
            "match_id": 1,
            "sender_id": 1,
            "message": "Hello!"
        })
        self.assertEqual(response.status_code, 200)  # Message should be accepted
