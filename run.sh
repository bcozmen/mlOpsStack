#!/bin/bash

# 1. Move to the project root directory
cd /var/www/mlOpsStack

# 2. Activate the virtual environment
source venv/bin/activate

# 3. Kill any existing processes on ports 8001 and 8002 to prevent crashes
echo "Cleaning up ports 8001 and 8002..."
sudo fuser -k 8001/tcp 2>/dev/null
sudo fuser -k 8002/tcp 2>/dev/null
sleep 1 # Give the system a second to breathe


# 4. Run Django on Port 8001 (in the background)
echo "Starting Django on port 8001..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput
nohup python manage.py runserver 0.0.0.0:8001 > django.log 2>&1 &

# 5. Run Uvicorn on Port 8002 (in the background)
echo "Starting Uvicorn backend on port 8002..."
# Note: `--reload` is removed to save your 1GB RAM VPS from freezing!
nohup python backend/mlops/main.py > uvicorn.log 2>&1 &

echo "----------------------------------------"
echo "Both servers are starting up in the background!"
echo "Check django.log and uvicorn.log for output."
echo "----------------------------------------"