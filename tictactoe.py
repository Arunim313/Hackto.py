#TicTacToe
import random
EMPTY ='[ ]'

def display_board(board):
    print() #bring the cursor on a new line
    for rows in board: #purple, blue, pink
        for cols in rows:
            print(cols, end= ' ')
        print() #line change

def is_full(board):
    #checks for an empty cell, if found then board is not full, otherwise full.
    for rows in board:
        for cols in rows:
            if cols == EMPTY:
                return False #not fulll
    return True #full

def toss():
    temp = random.randint(1,2) #generate either 1 or 2
    if temp == 1:
        return 'heads'
    else:
        return 'tails'

def validate_move(board, r, c):
    if r >=0 and r <=2: #row check
        if c >=0 and c <=2: #col check
           if board[r][c] == EMPTY: #data check
               return True #move is valid
    return False #move is invalid

def check_wins(board, symbol):
    #diagonal check
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    # reverse diagonal check
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    #rows check
    i = 0
    while i < 3: #0,1,2
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True
        i+=1
    #cols check
    i = 0
    while i < 3: #0,1,2
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
        i+=1

    #non of the above returned True, so it means that theres not a win yet
    return False

def clear_board(board):
    i =0
    while i < 3: #0,1,2
        j =0
        while j < 3:#0,1,2
            board[i][j] = EMPTY
            j+=1
        i+=1

def tictactoe():
    #board (nested list)
    row1 = [EMPTY, EMPTY, EMPTY] #purple (a list)
    row2 = [EMPTY, EMPTY, EMPTY] #blue (a list)
    row3 = [EMPTY, EMPTY, EMPTY] #pink (a list)
    board = [row1, row2, row3] #grey (a nested list)

    #set the players
    players = [] #empty list
    print('Enter name for player1 ')
    players.append(input().title()) #add name of player1 to the list
    print('Enter name for player2 ')
    players.append(input().title())#add name of player2 to the list

    #symbols
    symbols = ['[X]', '[O]'] #preset list

    play_again = True
    while play_again:
        #lets toss
        print(players[0], 'flips the coin')
        print(players[1], 'makes a call (heads/tails)')
        call = input().lower()
        result = toss()
        print('Result:', result)
        if call == result:
            current_player = 1 #players[1] will start the game
        else:
            current_player = 0 #players[0] will start the game

        print(players[current_player], 'will start the game')

        do_we_have_a_winner = False

        #lets play
        while not is_full(board):
            #render the board
            display_board(board)
            #play
            print(players[current_player],  symbols[current_player],  'plays')
            print('Enter the board co-ords to place:', symbols[current_player])
            print('Row (0-2):')
            r = int(input())
            print('Col (0-2):')
            c = int(input())

            if validate_move(board,r,c):
                #register the move
                board[r][c] = symbols[current_player]
                #check whether the player wins by this move
                if check_wins(board, symbols[current_player]):
                    do_we_have_a_winner = True
                    display_board(board)
                    print(players[current_player], symbols[current_player], 'WINS!!!')
                    break #stop the loop
                else:
                    #change the player
                    current_player = (current_player+1) % 2
            else:
                print('Invalid Move, Please Play Again!!!')

        if do_we_have_a_winner == False:
            display_board(board)
            print('Game DRAW!!!')

        print('Play gain (y/n)')
        if input().lower() == 'y':
            play_again = True
            clear_board(board)
        else:
            play_again = False

#program starts here
tictactoe()
