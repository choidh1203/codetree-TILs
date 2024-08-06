n = int(input())
dx = {'W':-1, 'S':0, 'N':0, 'E':1}
dy = {'W':0, 'S':-1, 'N':1, 'E':0}
nx, ny = 0, 0


for i in range(n):
    a, b = input().split()
    b = int(b)

    nx, ny = nx + b*dx.get(a), ny + b*dy.get(a)

print(nx,ny)