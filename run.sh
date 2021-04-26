#!/bin/bash
set -e
. ./backend/venv/bin/activate

cd backend/
pip install -r requirements.txt

export DEBUG=True

uvicorn main:app --reload
