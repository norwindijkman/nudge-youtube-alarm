# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import sys
import googleapiclient.discovery
from dotenv import load_dotenv
load_dotenv()

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ.get( "YOUTUBE_API_KEY" )
    CHANNEL_ID = sys.argv[1]
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
    request = youtube.search().list(
        part="snippet, id",
        channelId=CHANNEL_ID,
        order="date"
    )
    response = request.execute()
    print(response['items'][0]['id']['videoId'])

if __name__ == "__main__":
    main()
