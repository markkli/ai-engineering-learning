import re

url = input("URL: ").strip()

if match := re.search(r"^https?://(?:www\.)?twitter\.com/([^/]+)", url, re.IGNORECASE):
    print(f"Username: {match.group(1)}")