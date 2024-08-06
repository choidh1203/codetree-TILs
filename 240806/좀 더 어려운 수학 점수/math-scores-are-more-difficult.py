a, b = map(int,input().split())
c, d= map(int,input().split())

if a > c:
    print('A')
elif c > a:
    print('B')
elif b > d:
    print('A')
else:
    print('B')