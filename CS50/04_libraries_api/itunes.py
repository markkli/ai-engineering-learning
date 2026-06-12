import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Usage: python intro.py URL")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

data = response.json()
for result in data['results']:
    print(f"Track Name: {result['trackName']}")
    print(f"Artist Name: {result['artistName']}")
    print()