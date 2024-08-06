a, b = map(int,input().split())
c, d= map(int,input().split())

if b > d:
    print('A')
elif d > b:
    print('B')
elif a > c:
    print('A')
else:
    print('B')