# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] = > 0.19

import os

os.system('cls||clear')

user_list = [1.1, 1.2, 3.1, 5, 10.01]


def difference_max_and_min_in_fractional_in_list(list):
    new_list = []
    for i in list:
        new_list.append(round(i % 1, 5))
        if round(i % 1, 5) == 0:
            new_list.remove(new_list[-1])
    return max(new_list)-min(new_list)


print(difference_max_and_min_in_fractional_in_list(user_list))
