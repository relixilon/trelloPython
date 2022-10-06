# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests

url = "https://api.trello.com/1/lists/a63ssCxI/moveAllCards"

query = {
    'idBoard': 'A1ahOuEM',
    'idList': '5abbe4b7ddc1b351ef961414',
    'key': '856a573bdd993e3b151ffbe97404e229',
    'token': '6a7d8c5a016d4b4edc4346fa8d5848dd0dfb6c7778e7800223ed5837bf30907f'
}

response = requests.request(
    "POST",
    url,
    params=query
)

print(response.text)
