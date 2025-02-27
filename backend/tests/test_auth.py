import unittest
from backend.app import app

class AuthTestCase(unittest.TestCase):
    """
    Unit test case for the authentication system.

    - Tests the `/api/auth/register` and `/api/auth/login` endpoints.
    - Ensures users can register and log in successfully.
    """

    def setUp(self):
        """
        Sets up the test client before each test case.

        - Creates a test client for sending HTTP requests.
        - Ensures the app runs in testing mode.
        """
        self.client = app.test_client()

    def test_register_user(self):
        """
        Tests the user registration functionality.

        - Sends a `POST` request to `/api/auth/register` with a test username, email, and password.
        - Ensures the response status code is `201 Created` if registration is successful.
        """
        response = self.client.post('/api/auth/register', json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 201)  # User should be created successfully

    def test_login_user(self):
        """
        Tests the user login functionality.

        - Registers a new test user.
        - Sends a `POST` request to `/api/auth/login` with correct credentials.
        - Ensures the response status code is `200 OK` if login is successful.
        """
        # Register a user first to ensure login test works
        self.client.post('/api/auth/register', json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        })

        # Attempt to log in with the registered credentials
        response = self.client.post('/api/auth/login', json={
            "email": "test@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 200)  # Login should be successful
