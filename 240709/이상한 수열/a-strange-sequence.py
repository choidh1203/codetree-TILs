import math

def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n >= 3:
        return func(math.floor(n/3)) + func(n-1)

a = int(input())

print(func(a))