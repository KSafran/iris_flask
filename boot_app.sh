#! /bin/bash
source venv/bin/activate
exec gunicorn -w 4 -b :5000 run_flask:app
