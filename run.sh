#!/bin/bash

# 0. Configure Virtual Environment
echo "Configuring virtual environment..."
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
# Use . instead of source for better compatibility (e.g. with sh/dash)
. venv/bin/activate

# 1. Upgrade pip and Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

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
