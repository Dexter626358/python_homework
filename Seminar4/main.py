import random
# Урок 4. Данные, функции и модули в Python. Продолжение
# 1 Вычислить число π c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# https://completerepair.ru/kak-vychislit-chislo-pi

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

get_pi(0.01)
get_pi(0.001)
get_pi(0.0001)

# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]

def simple_multiplaier(num, lst=[]):
    if num == 1:
        return sorted(lst)
    count = 2
    while count <= num:
        if num % count == 0:
            lst.append(count)
            num //= count
            count += 1
        else:
            count += 1

    return simple_multiplaier(num)

print(simple_multiplaier(236))

# 3 Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

def get_unic_elements(lst):
    dict_freq = {}
    for i in lst:
        dict_freq[i] = lst.count(i)
    unic_elem = []
    for k, v in dict_freq.items():
        if v == 1:
            unic_elem.append(k)
    return unic_elem

print(get_unic_elements([1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]))


# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def create_polinomoal(k):
    powers = [i for i in range(k, 1, -1)]
    coefficients = [random.randint(2, 101) for i in range(1, k+1)]
    polinom = []
    for i in range(len(powers)):
        polinom.append(f"{coefficients[i]}*x^{powers[i]}")
    polinom.append(f"{coefficients[-1]}")
    polonom_str = " + ".join(polinom) + " = 0"
    with open("polinom", "a", encoding='utf-8') as file:
        file.write(polonom_str + "\n")
    return polonom_str

print(create_polinomoal(8))



# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными.
# Степени многочленов могут отличаться.

def read_file(path):
    with open(path, "r", encoding='utf-8') as file1:
        return file1.readline()

def add_sign_polinomial_term(polinom_lst):
    tmp_lst = []
    index = 0
    while index < len(polinom_lst):
        if polinom_lst[index] == "+" or polinom_lst[index] == "-":
            tmp_lst.append(polinom_lst[index] + polinom_lst[index + 1])
            index += 2
        else:
            tmp_lst.append(polinom_lst[index])
            index += 1
    return tmp_lst

def get_last_three_elements_with_gaps(polinom1_lst, polinom2_lst):
    last_three = [str(int(polinom1_lst[-3]) + int(polinom2_lst[-3])), " ", polinom1_lst[-2], " ",
                  str(int(polinom1_lst[-1]) + int(polinom2_lst[-1]))]
    return last_three

def get_result_list_polinom(sorted_dict, last_three):
    list_values = [i for i in sorted_dict.values()]
    final_lst = []
    for i in range(len(list_values)):
        number = int(list_values[i].split("*")[0])
        if i == 0:
            final_lst.append(list_values[i])
        else:
            if number < 0:
                number *= -1
                final_lst.append(" - ")
                final_lst.append(str(number) + "*" + list_values[i].split("*")[1])
            else:
                final_lst.append(" + ")
                final_lst.append(str(number) + "*" + list_values[i].split("*")[1])

    if int(last_three[0]) > 0:
        final_lst.append(" + ")
    else:
        final_lst.append(" - ")
        last_three[0] = str(int(last_three[0]) * -1)
    final_lst += last_three
    return final_lst

def creat_dictionary(lst):
    polinom_dict = {}
    for i in lst:
        polinom_dict[int(i[-1])] = i
    return polinom_dict

polinom1_lst = read_file("polinom1").split(" ")  # считывание многочлена в список
polinom2_lst = read_file("polinom2").split(" ")
tmp_lst = add_sign_polinomial_term(polinom1_lst)  #  добавление знака к членам первого многочлена
polinom1_lst.clear()
polinom1_lst = [i for i in tmp_lst] #  заполнение исходного списка измененными членами
tmp_lst = add_sign_polinomial_term(polinom2_lst) #  добавление знака к членам второго многочлена
polinom2_lst.clear()
polinom2_lst = [i for i in tmp_lst] #  заполнение исходного списка измененными членами
last_three = get_last_three_elements_with_gaps(polinom1_lst, polinom2_lst)
del polinom1_lst[-3::] #  удаление свободного члена, знака равенства и нуля из списка
del polinom2_lst[-3::]
polinom1_dict = creat_dictionary(polinom1_lst)
polinom2_dict = creat_dictionary(polinom2_lst)
polinom_sum_dict = {}
if len(polinom1_dict) > len(polinom2_dict):
    small_dict = polinom2_dict
    big_dict = polinom1_dict
else:
    small_dict = polinom1_dict
    big_dict = polinom2_dict
for i in small_dict.keys():
    if i in big_dict:
        sum = int(small_dict[i].split("*")[0]) + int(big_dict[i].split("*")[0])
        polinom_sum_dict[i] = str(sum) + "*" + small_dict[i].split("*")[1]
        big_dict.pop(i)
    else:
        polinom_sum_dict[i] = small_dict[i]
polinom_sum_dict.update(big_dict)
sorted_polinom_dict = dict(sorted(polinom_sum_dict.items(), reverse=True))
final_lst = get_result_list_polinom(sorted_polinom_dict, last_three) # список готовый для перевода в строку
join_polinomial = "".join(final_lst)
print(join_polinomial)
with open("polinom3", 'w', encoding='utf-8') as file:
     file.write(join_polinomial + "\n")




