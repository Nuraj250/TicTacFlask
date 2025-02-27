#!/bin/bash

# Print a message indicating the start of deployment
echo "🚀 Deploying Flask Backend..."

# Pull the latest code from the main branch
git pull origin main

# Install/update all required Python dependencies
pip install -r requirements.txt

# Initialize the database (ensures tables exist)
python backend/database/init_db.py

# Print a message indicating the deployment is complete
echo "✅ Deployment complete!"
