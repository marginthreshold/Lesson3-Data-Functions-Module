# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import os
os.system('cls||clear')

user_list = [2, 3, 5, 6]


def product_of_pairs_in_list(list):
    new_lst = []
    limit = (len(list)//2+1)
    if len(list) % 2 == 0:
        limit = len(list)//2
    for i in range(limit):
        new_lst.append(list[i]*list[-1-i])
    return new_lst


print(product_of_pairs_in_list(user_list))
