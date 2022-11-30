# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import os

os.system('cls||clear')

fibonacchi_limit = int(
    input('Введите номер числа в последовательности Фибоначчи: '))


def negative_to_positive_fibonachi_list(number):
    fibonachchi_list = [0]*(number*2+1)
    fibonachchi_list[number+1] = 1
    fibonachchi_list[number-1] = -1
    for i in range(1, number):
        fibonachchi_list[number+1+i] = fibonachchi_list[number+i] + fibonachchi_list[number+i-1]
        fibonachchi_list[number-1-i] = -fibonachchi_list[number+1+i]
    return fibonachchi_list

print(negative_to_positive_fibonachi_list(fibonacchi_limit))
