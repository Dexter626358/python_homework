import random
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def remove_words_with_substring(sentence_, substring):
    list_words = sentence_.split(" ")
    list_without_subs = []
    for word in list_words:
        if substring not in word:
            list_without_subs.append(word)
    return " ".join(list_without_subs)


sentence = "забвение слово без разделителя зимбабве незабвен забвенный незабвенен абв незабвенный самозабвенен" \
           "самозабвение зимбабвийский самозабвенный самозабвенность"
print(remove_words_with_substring(sentence, "абв"))

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


def print_game_state(candies, computer_score, player2_score):
    print(f"There are {candies} candies.")
    print(f"Computer has {computer_score} candies")
    print(f"You have {player2_score} candies")
    print()


def first_player():
    way = random.randint(0, 1)
    if way == 0:
        flag_ = False
    else:
        flag_ = True
    return flag_


flag = first_player()


def player(candies, player2_score):
    numbers = set([i for i in range(1, 29)])
    print("you are playing: ")
    print("Enter a number of candies:")
    ask_candies = input()
    if ask_candies.isdigit() and int(ask_candies) in numbers:
        if candies < int(ask_candies):
            print("There is not enough candies. Try again.")
            player(candies, player2_score)
        else:
            candies -= int(ask_candies)
            player2_score += int(ask_candies)
    else:
        print("Incorrect input. Try again")
        player(candies, player2_score)
    return candies, player2_score


def computer(candies, computer_score):
    print("computer is playing: ")
    if candies > 55:
        ask_candies = random.randint(1, 28)
        candies -= ask_candies
        computer_score += ask_candies
    elif candies > 28 and candies <= 55:
        ask_candies = candies % 28
        candies -= ask_candies
        computer_score += ask_candies
    else:
        computer_score += candies
        candies -= candies
    return candies, computer_score


candies = 2021
print(f"There are {candies} candies left")
computer_score = 0
player2_score = 0
end = True


# while end:
#     if flag:
#         candies, player2_score = player(candies, player2_score)
#         flag = False
#         print_game_state(candies, computer_score, player2_score)
#     else:
#         candies, computer_score = computer(candies, computer_score)
#         flag = True
#         print_game_state(candies, computer_score, player2_score)
#     if candies == 0:
#         if flag:
#             print("computer won")
#         else:
#             print("You won")
#         end = False


# Создайте программу для игры в ""Крестики-нолики"".


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
    count = 0
    for i in board:
        for j in i:
            if j == " ":
                count += 1
    x_win = board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" or \
            board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" or \
            board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" or \
            board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" or \
            board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" or \
            board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X" or \
            board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" or \
            board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"

    o_win = board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" or \
            board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" or \
            board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" or \
            board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" or \
            board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" or \
            board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O" or \
            board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" or \
            board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"
    if x_win != True and o_win != True and count == 0:
        print("Draw")
        return "Draw"
    if x_win:
        print("X wins")
        return "X wins"
    if o_win:
        print("O wins")
        return "O wins"
    if x_win != True and o_win != True and count > 0:
        print("Game not finished")
        return "Game not finished"



def player(possition, board):
    coordinates = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (2, 0),
                   "8": (2, 1), "9": (2, 2)}
    x = coordinates[possition][0]
    y = coordinates[possition][1]
    if board[x][y] == " ":
        board[x][y] = "X"
    else:
        print("This cell is already occupied. Try again")
    return board


def computer(board):
    coordinates = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (2, 0),
                   "8": (2, 1), "9": (2, 2)}
    possition = str(random.randint(1, 9))
    x = coordinates[possition][0]
    y = coordinates[possition][1]
    if board[x][y] == " ":
        board[x][y] = "O"
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
        if x_or_o:
            print("Enter coordinate from 1 to 9:")
            possition = input()
            possitions = [str(i) for i in range(1, 10)]
            if possition not in possitions:
                print("Incorrect. Try again.")
                continue
            else:
                board = player(possition, board)
                print_board(board)
                result = check_result_of_game(board)
                x_or_o = False
                if result == "Draw" or result == "X wins" or result == "O wins":
                    break
        else:
            print("computer is playing")
            board = computer(board)
            print_board(board)
            result = check_result_of_game(board)
            x_or_o = True
            if result == "Draw" or result == "X wins" or result == "O wins":
                break

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
symbols = "aaaaabbbbbbbbbbbbbbbbbbbbcccccc222222dddddddddddddddeeeee"


def compression(string):
    compression_list = []
    symbols_with_gaps = symbols + " "
    count = 1
    for i in range(0, len(symbols_with_gaps) - 1):

        if symbols_with_gaps[i] == symbols_with_gaps[i + 1]:
            count += 1
            if count == 9:
                # print(f"{symbols_with_gaps[i]}{count}", end="")
                compression_list.append(symbols_with_gaps[i])
                compression_list.append(str(count))
                count = 0
        else:
            # print(f"{symbols_with_gaps[i]}{count}", end="")
            compression_list.append(symbols_with_gaps[i])
            compression_list.append(str(count))
            count = 1
    return "".join(compression_list)


print(compression(symbols))

symbols1 = "a5b9b9b2c626d9d6e5"


def decompression(string):
    decompresssion_lst = []
    for i in range(0, len(symbols1) - 1, 2):
        decompresssion_lst.append(symbols1[i] * int(symbols1[i + 1]))
    return "".join(decompresssion_lst)


print(decompression(symbols1))

# 5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.

#lst = [1, 5, 2, 3, 4, 6, 1, 7]
with open('list', 'r', encoding='utf-8') as file:
    str_lst = file.read()
lst = str_lst.split(" ")

two_elms_lst = []
for i in range(len(lst)): # получение списка последовательностей из 2х элементов
    for j in range(i + 1, len(lst)):
        tmp = []
        tmp.append(lst[i])
        tmp.append(lst[j])
        for k in range(len(tmp) - 1):
            if tmp[k] < tmp[k + 1]:
                    two_elms_lst.append(tmp)


def get_sequances(two_elms_lst, lst): # получение всех остальных последовательностей
    length_last = len(two_elms_lst[-1])
    if length_last == 8:
        return two_elms_lst
    else:
        for k in two_elms_lst:
            if len(k) == length_last:
                index = two_elms_lst.index(k)
                break
        tmp_list = two_elms_lst[index::]
        for i in tmp_list:
            last_index_elm = lst.index(i[-1])
            for j in range(last_index_elm + 1, len(lst)):
                copy = i[::]
                copy.append(lst[j])
                two_elms_lst.append(copy)
    return get_sequances(two_elms_lst, lst)


get_sequances(two_elms_lst, lst)

result = []
for i in two_elms_lst:  # выбор возрастающих последовательностей
    for j in range(len(i) - 1):
        if i[j] < i[j + 1]:
            check_seq = True
        else:
            check_seq = False
            break
    if check_seq:
        result.append(i)

result_str = []
for i in result:
    result_str.append(str(i))
with open('sequences', 'w', encoding='utf-8') as file:
    file.write(" ".join(result_str))
print(len(result))
print(result)
