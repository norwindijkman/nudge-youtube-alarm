#!/bin/bash
input="${0%/*}/scheduled.txt"
CURRENT_DATE=$(date -u +"%F %H:%M:00")
echo "$CURRENT_DATE <- Startdate"
while IFS= read -r line
do
  SCHEDULED_DATE="$(echo "$line" | cut -d'+' -f1)"
  echo $SCHEDULED_DATE
  SCHEDULED_YOUTUBE_CHANNEL="$(echo "$line" | cut -d' ' -f3)"
  if [ "$CURRENT_DATE" = "$SCHEDULED_DATE" ]; then
      echo "Opening $SCHEDULED_YOUTUBE_CHANNEL"
      sh ./open-youtube-vid.sh $SCHEDULED_YOUTUBE_CHANNEL
  fi;
done < "$input"
