#!/bin/bash

settings=${1:-"archer.settings"}
ip=${2:-"0.0.0.0"}
port=${3:-8888}

gunicorn -w 2 --env DJANGO_SETTINGS_MODULE=${settings} --error-logfile=/tmp/archer.err -b ${ip}:${port} --daemon archer.wsgi:application
