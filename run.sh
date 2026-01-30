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
echo "Starting server on port 5001..."
# Kill any existing process on port 5001 (optional but safe)
lsof -ti:5001 | xargs -r kill -9

# Start with nohup using the virtual environment's python
# Use 'venv/bin/python3' explicitly to ensure we use the venv even inside nohup
nohup venv/bin/python3 manage.py runserver 0.0.0.0:5001 > runserver.log 2>&1 &

echo "=================================================="
echo "✅ Server started successfully!"
echo "📡 Access at: http://YOUR_SERVER_IP:5001/"
echo "📝 Logs are being written to: runserver.log"
echo "=================================================="
