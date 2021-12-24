import io
import json

import requests

url = "http://127.0.0.1:8000/api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data['id'] = id
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    print(data)

def post_data():
    data = {
        'name':'elric',
        'city':'ro',
        'roll':1222
    }
    json_data = json.dumps(data)
    r = requests.post(url = url,data = json_data)
    data= r.json()
    print(data)

get_data(1)
post_data()