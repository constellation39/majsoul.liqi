import json
from random import random

import requests


def fetch_json(url):
    try:
        print(f'Fetching {url}')
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'Request failed with error: {e}')
        return None


base_url = 'https://game.maj-soul.net/1/'

result = int(random() * 1e9) + int(random() * 1e9)
version_json = fetch_json(f'{base_url}version.json?randv={result}')
if not version_json:
    print('Failed to fetch version.json')
    exit(1)

assert 'version' in version_json
version = version_json["version"]
resversion_json = fetch_json(f'{base_url}resversion{version}.json')
if not resversion_json:
    print('Failed to fetch resversion.json')
    exit(1)

assert 'res' in resversion_json
assert 'res/proto/liqi.json' in resversion_json['res']
assert 'prefix' in resversion_json['res']['res/proto/liqi.json']
prefix = resversion_json['res']['res/proto/liqi.json']['prefix']
liqi_json = fetch_json(f'{base_url}{prefix}/res/proto/liqi.json')
if not liqi_json:
    print('Failed to fetch liqi.json')
    exit(1)

# write file liqi.json
with open('liqi.json', 'w') as f:
    json.dump(liqi_json, f)
