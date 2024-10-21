# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять

def num_wor(num):
    if num > 19:
        if num // 10 == 2:
            print('двадцать', end=" ")
        elif num // 10 == 3:
            print('тридцать', end=" ")
        elif num // 10 == 4:
            print('сорок', end=" ")
        elif num // 10 == 5:
            print('пятьдесят', end=" ")
        elif num // 10 == 6:
            print('шестьдесят', end=" ")
        elif num // 10 == 7:
            print('семьдесят', end=" ")
        elif num // 10 == 8:
            print('восемдесят', end=" ")
        elif num // 10 == 9:
            print('девяноста', end=" ")

        if num % 10 == 1:
            print('один')
        elif num % 10 == 2:
            print('два')
        elif num % 10 == 3:
            print('три')
        elif num % 10 == 4:
            print('четыре')
        elif num % 10 == 5:
            print('пять')
        elif num % 10 == 6:
            print('шесть')
        elif num % 10 == 7:
            print('семь')
        elif num % 10 == 8:
            print('восемь')
        elif num % 10 == 9:
            print('девять')
    elif num == 10:
        print('десять')
    elif 10 < num < 20:
        if num % 10 == 1:
            print('один', end='')
        elif num % 10 == 2:
            print('двe', end='')
        elif num % 10 == 3:
            print('три', end='')
        elif num % 10 == 4:
            print('четыре', end='')
        elif num % 10 == 5:
            print('пять', end='')
        elif num % 10 == 6:
            print('шесть', end='')
        elif num % 10 == 7:
            print('семь', end='')
        elif num % 10 == 8:
            print('восемь', end='')
        elif num % 10 == 9:
            print('девять', end='')
        print('надцать')
    elif num < 10:
        if num % 10 == 0:
            print('ноль', end='')
        if num % 10 == 1:
            print('один', end='')
        elif num % 10 == 2:
            print('два', end='')
        elif num % 10 == 3:
            print('три', end='')
        elif num % 10 == 4:
            print('четыре', end='')
        elif num % 10 == 5:
            print('пять', end='')
        elif num % 10 == 6:
            print('шесть', end='')
        elif num % 10 == 7:
            print('семь', end='')
        elif num % 10 == 8:
            print('восемь', end='')
        elif num % 10 == 9:
            print('девять', end='')


num = int(input())

num_wor(num)