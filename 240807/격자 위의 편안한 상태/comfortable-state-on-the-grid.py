n, m = map(int,input().split())
dx, dy = [1,0,-1,0],[0,1,0,-1]

arr = [[0]*n for _ in range(n)]

def in_range(x,y,n):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(m):
    y, x = map(int,input().split())

    arr[y-1][x-1] = 1
    cnt = 0
    for j in range(4):
        nx, ny = x-1+dx[j], y-1+dy[j]
        if in_range(nx,ny,n) and arr[ny][nx] == 1:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)