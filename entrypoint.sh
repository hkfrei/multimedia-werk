#!/bin/sh

# exit when failure occurs
set -e
uwsgi --http "0.0.0.0:${PORT}" --module website.wsgi --master --processes 4 --threads 2 --static-gzip-all --buffer-size 32768 --mime-file /app/mime.types --mime-file /etc/mime.types
