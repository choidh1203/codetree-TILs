arr = [[0]*2001 for _ in range(2001)]

offset = 1000

a_x1, a_y1, a_x2, a_y2 = tuple(map(int,input().split()))
b_x1, b_y1, b_x2, b_y2 = tuple(map(int,input().split()))


#색종이 칠하기
for y in range(a_y1+offset, a_y2+offset):
    for x in range(a_x1+offset, a_x2+offset):
        arr[y][x] = 1

for y in range(b_y1+offset, b_y2+offset):
    for x in range(b_x1+offset, b_x2+offset):
        arr[y][x] = 0 

#min_x, min_y, max_x, max_y 구하기
max_x, max_y = 0, 0
min_x, min_y = 2000, 2000

for y in range(a_y1+offset, a_y2+offset):
    for x in range(a_x1+offset, a_x2+offset):
        if arr[y][x] == 1:
            if x <= min_x:
                min_x = x
            
            if y <= min_y:
                min_y = y

            if x > max_x:
                max_x = x
            
            if y > max_y:
                max_y = y
        else:
            pass

print((max_x+1-min_x)*(max_y+1-min_y))