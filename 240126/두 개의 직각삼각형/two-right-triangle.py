n = int(input())
a = 0
for i in range(n):
    print("*"*n+" "*a+"*"*n)
    n -= 1
    a += 2