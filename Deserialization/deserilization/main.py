import json
import requests

url = "http://127.0.0.1:8000/api/"

data = {
    "name": "Elric",
    "roll": 100,
    "city": "Ranchi"
}
json_data = json.dumps(data)
r = requests.post(url=url, json=data)
print(r)
data = r.json()
print(data)
