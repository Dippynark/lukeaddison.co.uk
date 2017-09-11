#!/bin/bash
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
touch $SRCROOT/logs/gunicorn.log
touch $SRCROOT/logs/access.log
tail -n 0 -f $SRCROOT/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn lukeaddison_co_uk.wsgi:application \
    --name lukeaddison.co.uk \
    --bind 0.0.0.0:8000 \
    --workers 1 \
    --log-level=info \
    --log-file=$SRCROOT/logs/gunicorn.log \
    --access-logfile=$SRCROOT/logs/access.log \
    "$@"

