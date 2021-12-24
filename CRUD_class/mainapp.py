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
        'name': 'ooo',
        'city': 'la',
        'roll': 1
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    data = r.json()
    print(data)


def update_data():
    data = {
        'id': 1,
        'name': 'PPPranav'
    }
    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {
        'id': 2
    }
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)


get_data()
delete_data()
# update_data()
# post_data()
