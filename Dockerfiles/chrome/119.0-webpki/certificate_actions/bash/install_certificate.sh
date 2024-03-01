#!/bin/bash

DOWNLOADS_FOLDER="/home/selenium/Downloads"
INSTALL_CERTIFICATE_FILES="/home/selenium/certificate_actions/py/install_certificate.py"
FILE_TO_FIND="certificate.pfx"

while true; do
    if [ -f "$DOWNLOADS_FOLDER/$FILE_TO_FIND" ]; then
        echo "Found $FILE_TO_FIND in Downloads folder."

        echo "decoding certificate"

        base64 -d < $DOWNLOADS_FOLDER/certificate.pfx > $DOWNLOADS_FOLDER/decoded_certificate.pfx

        sleep 2

        echo "certificate decoded"
        break
    else
        echo "File $FILE_TO_FIND not found. Waiting..."
        sleep 2
    fi
done

echo "Run certificate installation"

python3 $INSTALL_CERTIFICATE_FILES

echo 'installed' > $DOWNLOADS_FOLDER/certificate_status.txt
