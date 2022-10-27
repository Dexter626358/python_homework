import random
import emoji

zero = emoji.emojize(':orange_circle:')
cross = emoji.emojize(':cross_mark:')
initial_board = [["-", "-", "-"],
                 ["-", "-", "-"],
                 ["-", "-", "-"]]


def star_game():
    way = random.randint(0, 1)
    if way == 0:
        flag_ = False
    else:
        flag_ = True
    return flag_


x_or_o = star_game()


def print_board(board):
    dash = "---------"
    print(dash)
    for i in range(len(board)):
        print("|", end="")
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print("|")
        print()
    print(dash)


def check_result_of_game(board):
    x_win = board[0][0] == cross and board[0][1] == cross and board[0][2] == cross or \
            board[1][0] == cross and board[1][1] == cross and board[1][2] == cross or \
            board[2][0] == cross and board[2][1] == cross and board[2][2] == cross or \
            board[0][0] == cross and board[1][0] == cross and board[2][0] == cross or \
            board[0][1] == cross and board[1][1] == cross and board[2][1] == cross or \
            board[0][2] == cross and board[1][2] == cross and board[2][2] == cross or \
            board[0][0] == cross and board[1][1] == cross and board[2][2] == cross or \
            board[0][2] == cross and board[1][1] == cross and board[2][0] == cross

    o_win = board[0][0] == zero and board[0][1] == zero and board[0][2] == zero or \
            board[1][0] == zero and board[1][1] == zero and board[1][2] == zero or \
            board[2][0] == zero and board[2][1] == zero and board[2][2] == zero or \
            board[0][0] == zero and board[1][0] == zero and board[2][0] == zero or \
            board[0][1] == zero and board[1][1] == zero and board[2][1] == zero or \
            board[0][2] == zero and board[1][2] == zero and board[2][2] == zero or \
            board[0][0] == zero and board[1][1] == zero and board[2][2] == zero or \
            board[0][2] == zero and board[1][1] == zero and board[2][0] == zero
    if x_win:
        return "X wins"
    if o_win:
        return "O wins"



def player(board):
    global zero, cross
    print("Enter coordinate from 1 to 9:")
    possition = input()
    possitions = [str(i) for i in range(1, 10)]
    if possition not in possitions:
        print("Incorrect. Try again.")
        player(board)
    coordinates = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (2, 0),
                   "8": (2, 1), "9": (2, 2)}
    x = coordinates[possition][0]
    y = coordinates[possition][1]
    if board[x][y] == " ":
        board[x][y] = cross
    else:
        print("This cell is already occupied. Try again")
        player(board)
    return board


def computer(board):
    global zero, cross
    coordinates = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (2, 0),
                   "8": (2, 1), "9": (2, 2)}
    possition = str(random.randint(1, 9))
    x = coordinates[possition][0]
    y = coordinates[possition][1]
    if board[x][y] == " ":
        board[x][y] = zero
    else:
        computer(board)
    return board


while True:
    print("The game is starting:")
    print("'1' - to continue, '0' - to stop the game.")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    continue_game = input()
    if continue_game == '1':
        print_board(initial_board)
    elif continue_game == '0':
        break
    else:
        print("Incorrect input")
        continue
    while True:
        result = check_result_of_game(board)
        count = 0
        for i in board:
            for j in i:
                if j == " ":
                    count += 1
        if count == 0 and result != 'X wins' and result != 'O wins':
            print('Draw')
            break
        else:
            if result == 'X wins':
                print('X wins')
                break
            elif result == 'O wins':
                print('O wins')
                break
            else:
                print('The game is not finished yet')
            if x_or_o:
                player(board)
                print_board(board)
                x_or_o = False
            else:
                print("computer is playing")
                computer(board)
                print_board(board)
                result = check_result_of_game(board)
                x_or_o = True


