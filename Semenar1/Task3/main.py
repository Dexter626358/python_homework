"""Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
точек в этой четверти (x и y)."""
#print("Введите номер координатной четверти:")
#coordinate_part = input()
def coordinate_part(coordinate_part):
    parts = ["1", "2", "3", "4"]
    if coordinate_part in parts:
        if coordinate_part == "1":
            diapazone = "x > 0 и y > 0"
        elif coordinate_part == "2":
            diapazone = "x < 0 и y > 0"
        elif coordinate_part == "3":
            diapazone = "x < 0 и y < 0"
        else:
            diapazone = "x > 0 и y < 0"
    else:
        diapazone = "Такой четверти не существует"

    return diapazone

for i in range(10):
    print(coordinate_part(str(i)))