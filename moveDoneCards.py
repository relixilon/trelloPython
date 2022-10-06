from funcs import *
from datetime import datetime

#BOARD = '9hJdRrlB'
BOARD = 'A1ahOuEM'


def moveDoneCards(board):
    lists = getLists(board)

    for i in lists:
        if i['name'].split()[0] == 'Done':
            doneName = i['name']

    date = str(datetime.today().strftime('%Y/%m/%d'))

    name = date + ' Done'

    for i in lists:
        if i['name'] == name:
            return 'list already exists'
    else:
        done = findListByName(doneName, getLists(board))
        newList = createList(name, board)
        moveAllCards(getCards(done['id']), newList['id'])


moveDoneCards(BOARD)
