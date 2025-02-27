from flask_jwt_extended import create_access_token

def generate_token(user_id):
    """
    Generates a JWT access token for a user.

    - Uses Flask-JWT-Extended to create a secure authentication token.
    - Associates the token's identity with the user's ID.

    Parameters:
    - user_id (int): The unique identifier of the user.

    Returns:
    - str: A JWT token string that can be used for authentication.

    Example Usage:
    ```
    access_token = generate_token(user.id)
    ```
    """
    return create_access_token(identity=user_id)
