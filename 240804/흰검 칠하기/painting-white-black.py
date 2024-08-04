n = int(input())

arr = [[0] for _ in range(100001)]

loc = 50000

for _ in range(n):
    x, d = tuple(input().split())
    x = int(x)

    if d == 'R':
        for i in range(loc, loc+x):
            arr[i].append(2)
        loc = loc+x-1
    else:
        for i in range(loc,loc-x,-1):
            arr[i].append(1)
        loc = loc-x+1

for i in range(100001):
    if arr[i].count(1) >= 2 and arr[i].count(2) >= 2:
        arr[i] = 3
    else:
        arr[i] = arr[i][-1]

print(arr.count(1),arr.count(2),arr.count(3))