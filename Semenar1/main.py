# checking weekend
""" Напишите программу, которая принимает на вход цифру, обозначающую день недели,
 и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет """

week_days = ['1', '2', '3', '4', '5', '6', '7']

print("Введите номер дня недели:")
number = input()
if number in week_days:
    if number in week_days[5::]:
        print("Да")
    else:
        print("Нет")
else:
    print("Такого дня не существует")