arr = [[0]*2001 for _ in range(2001)]

offset = 1000

ax1, ay1, ax2, ay2 = tuple(map(int,input().split()))
bx1, by1, bx2, by2 = tuple(map(int,input().split()))
mx1, my1, mx2, my2 = tuple(map(int,input().split()))

for y in range(ay1, ay2):
    for x in range(ax1, ax2):
        arr[y][x] = 1
for y in range(by1, by2):
    for x in range(bx1, bx2):
        arr[y][x] = 1
for y in range(my1, my2):
    for x in range(mx1, mx2):
        arr[y][x] = 0

ans = 0

for y in range(2001):
    for x in range(2001):
        if arr[y][x] == 1:
            ans += 1

print (ans)