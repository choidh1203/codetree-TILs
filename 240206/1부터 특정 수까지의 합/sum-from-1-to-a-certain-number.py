def a(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return int(s/10)

n = int(input())
print(a(n))