# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def sum_numbers(number):
    sum_digit = 0
    temp_list = []
    for i in number:
        if i.isdigit():
            temp_list.append(int(i))
    sum_digit = sum(temp_list)
    return sum_digit

print(sum_numbers("6782"))
print(sum_numbers("0,56"))
print(sum_numbers("3.141695"))
print(sum_numbers("0,0005"))

# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(number):
    mult_lst = []
    if number == 1:
        mult_lst.append(1)
    else:
        mult_lst.append(1)
        j = 0
        for i in range(2, number + 1):
            mult_lst.append(mult_lst[j] * i)
            j += 1
    return mult_lst

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072

def sequence(size):
    sequence_list = []
    for i in range(1, size + 1):
        sequence_list.append((1 + 1 / i) ** i)
    return round(sum(sequence_list), 3)

print(sequence(1))
print(sequence(2))
print(sequence(3))
print(sequence(4))
print(sequence(5))
print(sequence(6))

# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

def mult_indexes(size, index_1, index_2):
    elements = [i for i in range(-size, size + 1)]
    return elements[index_1] * elements[index_2]

print(mult_indexes(10, 3, 15))

#Задание 5 Реализуйте алгоритм перемешивания списка.



def rng():
    m = 2 ** 32
    a = 1103515245
    c = 12345
    rng.current = (a*rng.current + c) % m
    return rng.current/m

rng.current = 3


def random_list(lst):
    length = len(lst)
    cmt = 0
    for i in range(length):
        index = int(rng() * length)
        cmt = lst[i]
        lst[i] = lst[index]
        lst[index] = cmt
    return lst

print(random_list([6, 4, 7, 3, 8, 9, 1, 2, 5, 10]))