#!/bin/bash

# build_files.sh

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput

# Apply database migrations
python3.9 manage.py migrate