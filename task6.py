# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3
def nod(a, b):
    if b == 0:
        return a
    return nod(b, a%b)

n1 = int(input())
n2 = int(input())

def drb(n1, n2):
    print(n1//nod(n1, n2), n2//nod(n1, n2))
drb(n1, n2)