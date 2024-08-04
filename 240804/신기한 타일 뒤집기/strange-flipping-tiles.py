n = int(input())

arr = [0]*100001

loc = 50000

for _ in range(n):
    x, d = tuple(input().split())
    x = int(x)

    if d == 'R':
        for i in range(loc, loc+x):
            arr[i] = 2
        loc = loc+x-1
    else:
        for i in range(loc,loc-x,-1):
            arr[i] = 1
        loc = loc-x+1

print(arr.count(1), arr.count(2))