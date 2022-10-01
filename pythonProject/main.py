# 1. Напишите программу, которая определит позицию второго вхождения строки в
# списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# 2. Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

a = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

value = "qwe"
j = 0

for i in range(len(a)):
    if a[i] == value:
        j = j + 1
    if j == 2:
        print(i)
        break
else:
    print(-1)

a = ["123", "234", 123, "567", 'werwer', 33, '324', 'werwww']
value = 567


for i in range(len(a)):
    if type(a[i]) == int:
        if a[i] == value:
            print(f'Value found on position {i}')
            break
    elif type(a[i]) == str:
        if a[i].isdigit() and int(a[i]) == value:
            print(f'Value found on position {i}')
            break
else:
    print('Value not found')




