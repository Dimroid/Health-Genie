#!/usr/bin/env bash
echo "BUILD START"
# Exit on error
set -o errexit

apt install libavdevice-dev libavfilter-dev libavformat-dev
apt install libavcodec-dev libswresample-dev libswscale-dev
apt install libavutil-dev 

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
echo "BUILD END"
