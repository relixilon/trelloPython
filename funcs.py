import requests
import json

with open('./keys.json') as f:
    data = json.load(f)
    KEY = data["KEY"]
    TOKEN = data["TOKEN"]


def moveCard(cardId, listId):

    url = "https://api.trello.com/1/cards/"+cardId

    headers = {
        "Accept": "application/json"
    }

    query = {
        'idList': listId,
        'key': KEY,
        'token': TOKEN
    }

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )

    return json.loads(response.text)


def getCards(listId):

    url = "https://api.trello.com/1/lists/"+listId+"/cards"

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

    return json.loads(response.text)


def createList(name, boardId):
    url = "https://api.trello.com/1/boards/"+boardId+"/lists"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'name': name,
        'key': '856a573bdd993e3b151ffbe97404e229',
        'token': '6a7d8c5a016d4b4edc4346fa8d5848dd0dfb6c7778e7800223ed5837bf30907f'
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    return json.loads(response.text)


def getLists(boardId):
    url = "https://api.trello.com/1/boards/"+boardId+"/lists"

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

    return json.loads(response.text)


def updateList(listId, atribute, value):

    url = "https://api.trello.com/1/lists/"+listId

    query = {
        atribute: value,
        'key': KEY,
        'token': TOKEN
    }

    response = requests.request(
        "PUT",
        url,
        params=query
    )

    return response.text


def updateCardCoverColor(cardId, value):
    headers = {
        "Accept": "application/json"
    }

    url = "https://api.trello.com/1/cards/" + cardId + "/cover"

    params = {"key": KEY, "token": TOKEN, "value": {'idAttachment': None,
                                                    'color': value,
                                                    'idUploadedBackground': None,
                                                    'size': 'normal',
                                                    'brightness': 'light'}}

    response = requests.request("PUT", url, headers=headers, json=params)

    return json.loads(response.text)


def updateCardCoverBrightness(cardId, value):
    headers = {
        "Accept": "application/json"
    }

    url = "https://api.trello.com/1/cards/" + cardId + "/cover"

    params = {"key": KEY, "token": TOKEN, "value": {'idAttachment': None,
                                                    'color': None,
                                                    'idUploadedBackground': None,
                                                    'size': 'normal',
                                                    'brightness': value}}

    response = requests.request("PUT", url, headers=headers, json=params)

    return json.loads(response.text)


def findListByName(name, lists):
    for i in lists:
        if i['name'] == name:
            return i


def moveAllCards(cards, listId):
    for i in cards:
        moveCard(i["id"], listId)


def getPosNewList(lists):
    count = 0
    for i in lists:
        if not i['name'][0].isdigit():
            count += 1
    return count
