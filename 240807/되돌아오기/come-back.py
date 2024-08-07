n = int(input())

mapper = {'W':0, 'S':1 , 'N': 2, 'E':3}

dx, dy = [-1, 0, 0, 1],[0, -1, 1, 0]

x, y = 0, 0

t = 0
ans = 0

for i in range(n):
    a, b = input().split()

    b = int(b)

    move = mapper[a]
    for j in range(b):
        x, y = x + dx[move], y + dy[move]

        t += 1

        if x == 0 and y == 0:
            ans = True
            break
    if ans:
        break

print(t if ans else -1)