#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# Run seed data on first deploy
python seed_data.py
