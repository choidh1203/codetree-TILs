di = {'U':2, 'D':1, 'R':0, 'L':3}
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
n, t = map(int,input().split())

def in_range(x,y,n):
    return 1 <= x and x <= n and 1 <= y and y <= n

y,x, d = input().split()
y, x = int(y), int(x)

move = di[d]

for _ in range(t):
    nx, ny = x + dx[move], y + dy[move]
    if in_range(nx, ny, n):
        x, y = x + dx[move], y + dy[move]
    else:
        move = 3 - move

print(y,x)