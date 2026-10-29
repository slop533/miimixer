#!/bin/sh
cd "$(dirname "$0")"
python3 setup.py
(sleep 1; (xdg-open http://localhost:8000/mii-mixer-v6-local.html || open http://localhost:8000/mii-mixer-v6-local.html) >/dev/null 2>&1) &
python3 serve.py 8000
