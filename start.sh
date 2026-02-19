#!/usr/bin/env sh

# pfun-django/start.sh

set -e

cd app; uv run manage.py runserver 0.0.0.0:8000
