@echo off
cd /d "%~dp0"
py setup.py || python setup.py
start "" http://localhost:8000/mii-mixer-v6-local.html
py serve.py 8000 || python serve.py 8000
