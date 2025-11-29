#! /usr/bin/env bash

set -e
set -x

# Let the DB start
python williott/prestart.py

# Run migrations
alembic upgrade head

echo "Migrations done"
