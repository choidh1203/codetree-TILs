arr = [[0]*201 for _ in range(201)]

offset = 100

n = int(input())

for i in range(1,n+1):
    if i % 2 == 1:
        x1,y1, x2,y2 = tuple(map(int,input().split()))
        
        for y in range(y1+offset, y2+offset):
            for x in range(x1+offset, x2+offset):
                arr[y][x] = 1
    
    else:
        x1,y1, x2,y2 = tuple(map(int,input().split()))

        for y in range(y1+offset, y2+offset):
            for x in range(x1+offset, x2+offset):
                arr[y][x] = 2

ans = 0

for i in range(201):
    ans += arr[i].count(2)

print(ans)