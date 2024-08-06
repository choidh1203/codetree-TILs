di = {'U':2, 'D':1, 'R':0, 'L':3}
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
n, t = map(int,input().split())

arr = [[0]*n for _ in range(n)]

def in_range(x,y,n):
    return 0 <= x and x < n and 0 <= y and y < n

y,x, d = input().split()
y, x = int(y)-1, int(x)-1

s = 0

move = di[d]

while s < t:
    nx, ny = x + dx[move], y + dy[move]
    if in_range(nx, ny, n):
        x, y = x + dx[move], y + dy[move]
        s += 1
    else:
        move = 3 - move
        s += 1

print(y+1,x+1)