from funcs import *

BOARD = '9hJdRrlB'
#BOARD = 'A1ahOuEM'


def calcHours(boardId):
    lists = getLists(boardId)
    for i in lists:
        cards = getCards(i['id'])
        name = i['name'].split('-')[0]
        totalTime = 0
        for card in cards:
            time = (0, card['name'].split()[-1]
                    )[card['name'].split()[-1].isdigit()]
            totalTime += int(time)
        updateList(i['id'], 'name', name + '- ' + str(totalTime))


calcHours(BOARD)
