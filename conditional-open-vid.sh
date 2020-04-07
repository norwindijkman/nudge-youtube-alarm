#!/bin/bash
input="${0%/*}/scheduled.txt"
CURRENT_DATE=$(date +"%FT%H:%M:00")
while IFS= read -r line
do
  SCHEDULED_DATE="$(echo "$line" | cut -d'+' -f1)"
  SCHEDULED_YOUTUBE_CHANNEL="$(echo "$line" | cut -d' ' -f2)"
  if [ "$CURRENT_DATE" = "$SCHEDULED_DATE" ]; then
      sh ./open-youtube-vid.sh $SCHEDULED_YOUTUBE_CHANNEL
  fi;
done < "$input"
