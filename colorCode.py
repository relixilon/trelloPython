from funcs import *

BOARD = '9hJdRrlB'


def colorCode(boardId):
    lists = getLists(boardId)
    for i in lists:
        cards = getCards(i['id'])
        for card in cards:
            place = card['name'].split()[0]
            match place:
                case "CASA":
                    updateCardCoverColor(card['id'], 'sky')
                case "CASTILLO":
                    updateCardCoverColor(card['id'], 'red')
                case "ISABEL":
                    updateCardCoverColor(card['id'], 'blue')
                case "SANTA":
                    updateCardCoverColor(card['id'], 'pink')
                case "SAN":
                    updateCardCoverColor(card['id'], 'yellow')
                case "SARDOY":
                    updateCardCoverColor(card['id'], 'lime')
                case "OFICINA":
                    updateCardCoverColor(card['id'], 'red')
                case "MARQUES":
                    updateCardCoverColor(card['id'], 'purple')
                case "BRO":
                    updateCardCoverColor(card['id'], 'black')
                    updateCardCoverBrightness(card['id'], 'dark')
                case "CONTINENTAL":
                    updateCardCoverColor(card['id'], 'orange')
                case "JAUJA":
                    updateCardCoverColor(card['id'], 'green')

                # x = updateCardCoverColor(card['id'], 'red')
colorCode(BOARD)
