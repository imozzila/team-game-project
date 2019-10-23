"""Tic tac toe"""

import random
board = [[0,1,2],
        [3,4,5],
        [6,7,8]]

# row = num // 3


def game_loop(board):
    player_moves = []
    cpu_moves = []
    game_end = False
    print_board(board)

    while not game_end:
        new_board, player_move = player_turn()
        player_moves.append(player_move)
        print_board(board)
        if check_Win("0", board):
            print("YOU WIN!!!")
            return True
        elif check_Win("0", board) == False:
            print("YOU DREW???")
            return True

        print()
        print()

        enemy_turn(board)
        print_board(board)
        if check_Win("X", board):
            print("YOU LOSE!!!!")
            return False





def enemy_turn(board):
    valid_move = False
    while not valid_move:
        row = random.randint(0,2)
        column = random.randint(0,2)
        if check_If_Valid_Move(row, column, board):
            valid_move = True
            board[row][column] = "X"


def get_index(board, player_move):
    for list in board:
        column = -1
        for value in list:
            column += 1
            if player_move == value:
                return (player_move//3) , column
            

def player_turn():
    valid_move = False
    while not valid_move:
        player_move = int(input("Enter a move"))
        row, column = get_index(board, player_move)
        if check_If_Valid_Move(row, column, board):
            valid_move = True
            board[row][column] = "O"


    return board, player_move

def check_Win(symbol, board):
    #Checking Horizontals
    for list in board:
        count = 0
        for value in list:
            if value == symbol:
                count += 1
    if count == 3:
        return True

    #Check Verticals
    for i in range(3):
        count = 0
        for list in board:
            if list[i] == symbol:
                count+= 1
                if count == 3:
                    return True

    #Checking Diags
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        return True

    count = 0
    for list in board:
        for value in list:
            if type(value) == str:
                count+=1
    if count == 9:
        return False

board = [[0,1,2],
        [3,4,5],
        [6,7,8]]


def check_If_Valid_Move(move_row, move_column, board):
    if board[move_row][move_column] == ("X" or "O"):
        print("Not a valid move")
        return False
    else:
        print("Valid Move")
        return True

def print_board(board):
    for row in board:
        print(row)

game_loop(board)
