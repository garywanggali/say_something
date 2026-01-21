#!/bin/bash

# 1. Install dependencies
echo "Installing dependencies..."
python3 -m pip install -r requirements.txt

# 2. Make and Apply database migrations
echo "Applying migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

# 3. Create default admin if not exists
echo "Checking admin user..."
python3 init_admin.py

# 4. Start the server
echo "Starting server..."
python3 manage.py runserver 0.0.0.0:8000
