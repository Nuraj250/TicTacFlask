from flask import Blueprint, request, jsonify
from backend.models.user import User
from backend.utils.db import db
from flask_jwt_extended import create_access_token
from flask_bcrypt import Bcrypt

# Initialize Bcrypt for password hashing
bcrypt = Bcrypt()

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Handles user registration.

    - Receives username, email, and password from the client.
    - Hashes the password using Bcrypt for security.
    - Stores the new user in the database.
    - Returns a success message upon successful registration.

    Expected Request Format (JSON):
    {
        "username": "player1",
        "email": "player1@example.com",
        "password": "securepassword"
    }

    Response Format (JSON):
    {
        "message": "User registered successfully!"
    }

    Returns:
    - 201 Created: If the user is successfully registered.
    """
    data = request.get_json()

    # Hash the password before storing it
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    # Create a new user instance
    user = User(username=data['username'], email=data['email'], password_hash=hashed_password)

    # Save user to the database
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Handles user login.

    - Checks if the provided email exists in the database.
    - Verifies the provided password using Bcrypt.
    - If successful, generates a JWT access token.
    - Returns the access token and username.

    Expected Request Format (JSON):
    {
        "email": "player1@example.com",
        "password": "securepassword"
    }

    Response Format (JSON):
    {
        "access_token": "<JWT_TOKEN>",
        "username": "player1"
    }

    Returns:
    - 200 OK: If login is successful.
    - 401 Unauthorized: If credentials are incorrect.
    """
    data = request.get_json()

    # Find the user by email
    user = User.query.filter_by(email=data['email']).first()

    # Verify password and generate access token if valid
    if user and bcrypt.check_password_hash(user.password_hash, data['password']):
        access_token = create_access_token(identity=user.id)  # Generate JWT token
        return jsonify({"access_token": access_token, "username": user.username}), 200

    # Return error if authentication fails
    return jsonify({"message": "Invalid credentials!"}), 401
