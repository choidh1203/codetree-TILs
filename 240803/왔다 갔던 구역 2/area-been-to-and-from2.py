arr = [0]*201
n = int(input())

loc = 100


for _ in range(n):
    x, d = tuple(input().split())
    
    x = int(x)

    if d == 'R':
        for i in range(loc, loc+x):
            arr[i] += 1
        loc = loc+x
    
    else:
        for i in range(loc-1, loc-x-1, -1):
            arr[i] += 1
        loc = loc-x

max_point = max(arr)
min_point = 2
ans = 0

for point in range(max_point, 1,-1):
    ans += arr.count(point)

print(ans)