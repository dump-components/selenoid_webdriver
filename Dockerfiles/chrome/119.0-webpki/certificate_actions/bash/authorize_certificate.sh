#!/bin/bash

LOCK_FILE="/home/selenium/Downloads/authorize_certificate.lock"
PYTHON_SCRIPT="/home/selenium/certificate_actions/py/authorize_certificate.py"

touch "$LOCK_FILE"

while true; do
    if [ ! -f "$LOCK_FILE" ]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') - Lock file not found. Executing Python script..."
        
        python "$PYTHON_SCRIPT" && echo "Script executed successfully." || echo "Failed to execute script."
        touch "$LOCK_FILE"
        
        echo "Lock file created at $LOCK_FILE."
    else
        echo "Lock file exists. Skipping execution."
    fi
    
    sleep 2
done
