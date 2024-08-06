di = {'U':2, 'D':1, 'R':0, 'L':3}
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
n, t = map(int,input().split())

arr = [[0]*n for _ in range(n)]

def in_range(x,y,n):
    return 0 <= x and x < n and 0 <= y and y < n

x,y, d = input().split()
x, y = int(x), int(y)

s = 0

move = di[d]

while s < t:
    x, y = x + dx[move], y + dy[move]
    s += 1
    if not in_range(x,y,n):
        move = 3 - move
        s += 1

print(x+1,y+1)