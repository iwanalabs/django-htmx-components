#!/bin/bash
set -e

source config.sh

# Define the command to add
JOB="*/5 * * * * $PROJECT_DIR/.venv/bin/python $PROJECT_DIR/$PROJECT_SUBDIR/manage.py regenerate_data"

# Check if the job already exists
(crontab -l | grep -q "$JOB") && echo "Cron job already exists" || (crontab -l 2>/dev/null; echo "$JOB") | crontab -

# Confirmation message
echo "Cron job added successfully"
