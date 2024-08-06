n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

dx, dy = [1,0,-1,0], [0,1,0,-1]

def in_range(x,y,n):
    return 0 <= x and x < n and 0 <= y and y < n

ans = 0

for y in range(n):
    for x in range(n):
        cnt = 0

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if in_range(nx,ny,n) and arr[ny][nx] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)