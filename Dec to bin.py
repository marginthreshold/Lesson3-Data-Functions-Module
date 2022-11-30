# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
import math
import os

os.system("cls||clear")

decimal = int(input("Введите число в десятичной системе: "))


def dec_to_bin(decimal_number):
    bin = 0
    for i in range(int(math.log2(decimal_number))+1):
        bin = bin+(decimal_number % 2*(10**i))
        decimal_number = decimal_number//2
    return bin


print(dec_to_bin(decimal))
