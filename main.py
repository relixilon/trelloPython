# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://api.trello.com/1/boards/A1ahOuEM"

headers = {
    "Accept": "application/json"
}

query = {
    'key': '856a573bdd993e3b151ffbe97404e229',
    'token': '6a7d8c5a016d4b4edc4346fa8d5848dd0dfb6c7778e7800223ed5837bf30907f'
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
)

print(json.dumps(json.loads(response.text),
      sort_keys=True, indent=4, separators=(",", ": ")))
