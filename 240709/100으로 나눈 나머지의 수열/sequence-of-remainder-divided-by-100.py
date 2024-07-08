def func(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    elif n >= 3:
        return (func(n-1)*func(n-2))%100

a = int(input())

print(func(a))