#!/bin/bash
VIDEO_ID=$("${0%/*}"/venv/bin/python "${0%/*}"/youtube-video-id-gen.py $1)
VIDEO_URL="https://youtube.com/watch?v=${VIDEO_ID}"
google-chrome-stable $VIDEO_URL
