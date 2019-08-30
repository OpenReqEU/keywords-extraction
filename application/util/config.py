import json


def get_ip():
    with open('config.json') as json_file:
        data = json.load(json_file)
        return data['ip']
