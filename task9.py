# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!

N = int(input())
c = 2
def step(N, c):
    if N == 1:
        return('YES')
    else:
        if c <= N:
            if N == c:
                return('YES')
            else:
                c *= 2
                return(step(N, c))
        else:
            return('NO')

print(step(N, c))