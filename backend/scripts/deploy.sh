#!/bin/bash
echo "🚀 Deploying Flask Backend..."
git pull origin main
pip install -r requirements.txt
python backend/database/init_db.py
echo "✅ Deployment complete!"
