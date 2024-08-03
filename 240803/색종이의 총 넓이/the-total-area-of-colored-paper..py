arr = [[0]*201 for i in range(201)]

n = int(input())

for i in range(n):
    x1, y1 = tuple(map(int,input().split()))
    x2, y2 = x1+8, y1+8

    for y in range(y1,y2):
        for x in range(x1, x2):
            arr[y][x] = 1

ans = 0

for i in range(201):
    ans += arr[i].count(1) 

print(ans)