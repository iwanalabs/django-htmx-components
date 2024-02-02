#!/bin/bash
set -e

source config.sh

JOB="*/5 * * * * $PROJECT_DIR/.venv/bin/python $PROJECT_DIR/$PROJECT_SUBDIR/manage.py regenerate_data"

echo "Adding the following cron job:"
echo "$JOB"

(crontab -l | grep -q "$JOB") && echo "Cron job already exists" || (crontab -l 2>/dev/null; echo "$JOB") | crontab -

echo "Cron job added successfully"
