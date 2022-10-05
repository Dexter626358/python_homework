# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst_number = [2, 3, 5, 9, 3]
lst_number1 = [i for i in range(101)]
def find_sum_odd_possition(lst):
    sum = 0
    odd_lst = lst[1::2]
    for i in odd_lst:
        sum += i
    return sum

print(find_sum_odd_possition(lst_number))
test1_1 = find_sum_odd_possition(lst_number) == 12
test1_2 = find_sum_odd_possition(lst_number1) == 2500
print(f"test1_1: {test1_1}")
print(f"test1_2: {test1_2}")

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mult_pair_numbers(lst):
    temp_list = []
    j = len(lst) - 1
    if len(lst) % 2 == 0:
        length = int(len(lst) / 2)
    else:
        length = int(len(lst) / 2) + 1
    for i in range(length):
        temp_list.append(lst[i] * lst[j])
        j -= 1
    return temp_list
test2_1 = mult_pair_numbers([2, 3, 4, 5, 6]) == [12, 15, 16]
test2_2 = mult_pair_numbers([2, 3, 5, 6]) == [12, 15]
print(f"test2_1: {test2_1}")
print(f"test2_2: {test2_2}")

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def get_difference_fractional(lst):
    fractional_lst = []
    for i in lst:
        if "." in str(i):
            fractional_part = str(i).split(".")[1]
            length_fractional_part = len(fractional_part)
            fractional_lst.append(int(fractional_part) / (10 ** length_fractional_part))
    return max(fractional_lst) - min(fractional_lst)

test3_1 = get_difference_fractional([1.1, 1.2, 3.1, 5, 10.01]) == 0.19
test3_2 = get_difference_fractional([1.1, 1.23, 3.106, 5, 10.0311, 5.0]) == 0.23
print(f"test3_1: {test3_1}")
print(f"test3_2: {test3_2}")

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_bin(number):
    temp_lst = []
    bin_number = ""
    while number != 0:
        temp_lst.append(number % 2)
        number //= 2
    for i in reversed(temp_lst):
        bin_number += str(i)
    return bin_number

test4_1 = ("0b" + decimal_to_bin(45) == bin(45))
test4_2 = ("0b" + decimal_to_bin(11) == bin(11))
test4_3 = ("0b" + decimal_to_bin(10) == bin(10))
test4_4 = ("0b" + decimal_to_bin(10456) == bin(10456))
print(f"test4_1: {test4_1}")
print(f"test4_2: {test4_2}")
print(f"test4_3: {test4_3}")
print(f"test4_4: {test4_4}")

# 4. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(number):
    if number < 3:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

def nega_fibonacci(number):
    if number == -1:
        return 1
    elif number == -2:
        return -1
    else:
        return nega_fibonacci(number + 2) - nega_fibonacci(number + 1)

def nega_fib(number):
    nega_fib_list = []
    for i in range(-number, 0):
        nega_fib_list.append(nega_fibonacci(i))
    nega_fib_list.append(0)
    for i in range(1, number + 1):
        nega_fib_list.append(fibonacci(i))
    return nega_fib_list

test5_1 = (nega_fib(8) == [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21])
print(f"test5_1: {test5_1}")




