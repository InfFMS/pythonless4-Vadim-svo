# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII

def rim(num):
    r_num = ""

    # Определяем соответствие чисел и римских символов через условия
    if num >= 1000:
        c = num // 1000
        r_num += "M" * c
        num %= 1000

    if num >= 900:
        r_num += "CM"
        num -= 900

    if num >= 500:
        r_num += "D"
        num -= 500

    if num >= 400:
        r_num += "CD"
        num -= 400

    if num >= 100:
        c = num // 100
        r_num += "C" * c
        num %= 100

    if num >= 90:
        r_num += "XC"
        num -= 90

    if num >= 50:
        r_num += "L"
        num -= 50

    if num >= 40:
        r_num += "XL"
        num -= 40

    if num >= 10:
        c = num // 10
        r_num += "X" * c
        num %= 10

    if num >= 9:
        r_num += "IX"
        num -= 9

    if num >= 5:
        r_num += "V"
        num -= 5

    if num >= 4:
        r_num += "IV"
        num -= 4

    if num >= 1:
        r_num += "I" * num

    return r_num


# Пример использования
num = int(input())

print(rim(num), end='')  # Вывод: MMXIII