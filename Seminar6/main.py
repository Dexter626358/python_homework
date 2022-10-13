import random

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


# использование list comprehension

print(sum([item for ind, item in enumerate(lst_number) if ind % 2 != 0]))
print(find_sum_odd_possition(lst_number))


# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def create_polinomoal(k):
    powers = [i for i in range(k, 1, -1)]
    coefficients = [random.randint(2, 101) for i in range(1, k + 1)]
    polinom = []
    for i in range(len(powers)):
        polinom.append(f"{coefficients[i]}*x^{powers[i]}")
    polinom.append(f"{coefficients[-1]}")
    polonom_str = " + ".join(polinom) + " = 0"
    with open("polinom", "a", encoding='utf-8') as file:
        file.write(polonom_str + "\n")
    return polonom_str


print(create_polinomoal(8))


# использование zip


def create_polinomoal(k):
    powers = [i for i in range(k, 1, -1)]
    coefficients = [random.randint(2, 101) for i in range(1, k + 1)]
    polinom = [(str(coef) + "*x^" + str(pow)) for pow, coef in zip(powers, coefficients)]
    polinom.append(f"{coefficients[-1]}")
    polonom_str = " + ".join(polinom) + " = 0"
    with open("polinom", "a", encoding='utf-8') as file:
        file.write(polonom_str + "\n")
    return polonom_str


print(create_polinomoal(8))

symbols1 = "a5b9b9b2c626d9d6e5"


# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
sentence = "забвение слово без разделителя зимбабве незабвен забвенный незабвенен абв незабвенный самозабвенен" \
           "самозабвение зимбабвийский самозабвенный самозабвенность"
substring = "абв"

def remove_words_with_substring(sentence_, substring):
    list_words = sentence_.split(" ")
    list_without_subs = []
    for word in list_words:
        if substring not in word:
            list_without_subs.append(word)
    return " ".join(list_without_subs)

# использование filter

split_sentence = sentence.split(" ")
print(" ".join(list(filter(lambda str: substring not in str, split_sentence))))

def get_pi(d):
    accurancy = 2
    while d != 1:
        d *= 10
        accurancy += 1
    pi4 = 1
    for i in range(1, 10000000):
        pi4 += 1/(2 * i + 1) * (-1) ** i
    pi = pi4 * 4
    pi_str = str(pi)
    print(f"Число PI c точностью до {accurancy - 2} знаков составляет: {float(pi_str[0:accurancy])}")

# использование map
range_numbers = [i for i in range(1, 10_000_000)]
d = 0.0001
pi4 = sum(list(map(lambda x: 1/(2 * x + 1) * (-1) ** x, range_numbers))) + 1
pi = pi4 * 4


def get_pi_1(d, pi):
    accurancy = 2
    while d != 1:
        d *= 10
        accurancy += 1
    pi_str = str(pi)
    print(f"Число PI c точностью до {accurancy - 2} знаков составляет: {float(pi_str[0:accurancy])}")

get_pi(d)
get_pi_1(d, pi)
