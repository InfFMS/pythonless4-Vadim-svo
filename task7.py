# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.

a = int(input())
b = int(input())
c = int(input())
def tri(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return(True)
    else: return(False)

print(tri(a, b, c))