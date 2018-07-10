import requests
import json

with open("config.json") as f:
    config = json.load(f)

url = f"https://transportapi.com/v3/uk/bus/stop/{config['ATCO']}/live.json"
params = {"app_id": config["app_id"], "app_key": config["app_key"]}
data = requests.get(url, params=params)
js = data.json()
print(js)

print(f"Next Depatrure: {js['departures']['85'][0]['aimed_departure_time']}")
