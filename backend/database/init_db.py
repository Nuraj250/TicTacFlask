from backend.app import app
from backend.utils.db import db

# Create a Flask application context to interact with the database
with app.app_context():
    db.create_all()  # Create all tables based on the defined models
    print("✅ Database initialized!")  # Confirmation message
