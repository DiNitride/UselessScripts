import requests
import sys
import urllib

if len(sys.argv) != 2:
    print("Usage: python countDownloads.py url")
    exit(1)

RELEASES_URL = "https://api.github.com/repos/{}/{}/releases"
user, repo = urllib.parse.urlparse(sys.argv[1]).path.strip("/").split("/")
releases = 0
assets = 0
downloads = 0


r = requests.get(RELEASES_URL.format(user, repo))
if r.status_code != 200:
    print(f"Error making GET request to Github API\nStatus: {r.status_code}\n" \
    f"Error: {r.json()['message']}\n" \
    f"Using the script on a private repo will return a 404")
    exit(1)

for r in r.json():
    # Each release
    releases += 1
    assets += len(r["assets"])
    for a in r["assets"]:
        # Each asset
        downloads += a["download_count"]

print(f"{user}/{repo} Download Data\n" \
    f"Total Releases: {releases}\n" \
    f"Total Assets: {assets}\n" \
    f"Total Downloads: {downloads}")
