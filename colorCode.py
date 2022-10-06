from funcs import *

BOARD = '9hJdRrlB'


def colorCode(boardId):
    lists = getLists(boardId)
    for i in lists:
        cards = getCards(i['id'])
        for card in cards:
            place = card['name'].split()[0]
            if place == "CASA":
                updateCardCoverColor(card['id'], 'sky')
            if place == "CASTILLO":
                updateCardCoverColor(card['id'], 'red')
            if place == "ISABEL":
                updateCardCoverColor(card['id'], 'blue')
            if place == "SANTA":
                updateCardCoverColor(card['id'], 'pink')
            if place == "SAN":
                updateCardCoverColor(card['id'], 'yellow')
            if place == "SARDOY":
                updateCardCoverColor(card['id'], 'lime')
            if place == "OFICINA":
                updateCardCoverColor(card['id'], 'red')
            if place == "MARQUES":
                updateCardCoverColor(card['id'], 'purple')
            if place == "BRO":
                updateCardCoverColor(card['id'], 'black')
                updateCardCoverBrightness(card['id'], 'dark')
            if place == "CONTINENTAL":
                updateCardCoverColor(card['id'], 'orange')
            if place == "JAUJA":
                updateCardCoverColor(card['id'], 'green')


colorCode(BOARD)
