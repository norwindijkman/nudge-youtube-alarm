#!/bin/bash
"${0%/*}"/venv/bin/python "${0%/*}"/retrieve-google-cal.py > "${0%/*}"/scheduled.txt
