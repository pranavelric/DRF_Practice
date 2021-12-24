import requests
import json

url = "http://127.0.0.1:8000/api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
        # data['id'] =id

    json_data = json.dumps(data)

    r = requests.get(url=url, data=json_data)

    data = r.json()
    print(data)


def post_data():
    data = {
        'name': 'Elric',
        'city': 'Sog',
        'roll': 1233
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    data = r.json()
    print(data)


# update
def update_data():
    data = {
        'id': 4,
        'name': 'Naruto',
        'city': 'Oog'
    }
    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {
        'id': 3
    }
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)


get_data(1)
delete_data()
# post_data()
# update_data()
