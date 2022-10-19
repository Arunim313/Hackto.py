#Tick toe by ved

import random

def start_player():

    startplayer = random.randint(1,2)
    if startplayer == 1:
        turn = 'X'
        print("Player One (X) will start the game.")
    else:
        startplayer == 2
        turn = 'O'
        print("Player Two (O) will start the game.")
    return turn

def getmove():

    row = int(input("Please enter a row number between 0 and 2: "))
    column = int(input("Please enter a column number between 0 and 2: "))
    while grid[row][column] != "":
        print("Invalid move.")
        row = int(input("Please enter a row number between 0 and 2: "))
        column = int(input("Please enter a column number between 0 and 2: ")) 
    return row, column

def mainturn(row, column):

    global countmove
    countmove = countmove + 1
    global symbol
    grid[row][column] = symbol

    for y in range(0,(len(grid))):
        print(grid[y])
    if symbol == 'X':
        symbol = 'O'
    elif symbol == 'O':
        symbol = 'X'
    return countmove

def check_win(row, column, symbol):    

    if (grid[0][0] and grid[0][1] and grid[0][2] == symbol) or (grid[1][0] and grid[1][1] and grid[1][2] == symbol) or (grid[2][0] and grid[2][1] and grid[2][2] == symbol) or (grid[0][0] and grid[1][0] and grid[2][0] == symbol) or (grid[0][1] and grid[1][1] and grid[2][1] == symbol)or (grid[0][2] and grid[1][2] and grid[2][2] == symbol)or (grid[0][0] and grid[1][1] and grid[2][2] == symbol) or (grid[2][0] and grid[1][1] and grid[0][2] == symbol):
        print("Well done!",symbol," won the game.")
        return true
        input('Press any key to continue...')
    elif countmove == 9:
        print("Board Full. Game over.")


#main program
grid = [["","",""],["","",""],["","",""]]

countmove = 0
win = 'false'

for y in range(0,(len(grid))):

    print(grid[y])

symbol = start_player()

while countmove != 9 or win == 'false':

    countmove = 0
    row, column = getmove()
    mainturn(row,column)
    win = check_win(row,column, symbol)
