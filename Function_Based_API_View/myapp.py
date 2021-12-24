import json

import requests
import io

url = "http://127.0.0.1:8000/api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data['id'] = id
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.get(url=url, headers=headers, data=json_data)
    data = r.json()
    print(data)


get_data()
