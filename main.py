#!/usr/bin/python
# encoding: utf-8
# Sven Behrens
import sys
import requests
import json

API_KEY = sys.argv[1]
CHANNEL_ID = sys.argv[2]


def get_channel_stat() -> dict:
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}'
    r = requests.get(url)
    data = r.json()
    return data['items'][0]['statistics']


stats = get_channel_stat()
subscribers = stats.get('subscriberCount')
views = stats.get('viewCount')
videos = stats.get('videoCount')

result = {"items": [
    {
        "type": "file",
        "title": subscribers,
        "subtitle": "Subscribers now!",
        "arg": subscribers
    },
    {
        "type": "file",
        "title": views,
        "subtitle": "Views now!",
        "arg": views
    },
    {
        "type": "file",
        "title": videos,
        "subtitle": "videos now!",
        "arg": videos
    }
]}

final_result = json.dumps(result)

print(final_result)
