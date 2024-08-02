n = int(input())

arr = [[0]*201 for _ in range(201)]

offset = 100

for i in range(n):
    x1,y1,x2,y2 = tuple(map(int,input().split()))

    for j in range(x1+offset,x2+offset):
        for k in range(y1+offset, y2+offset):
            arr[k][j] = 1

cnt = 0

for i in range(201):
    cnt += arr[i].count(1)

print(cnt)