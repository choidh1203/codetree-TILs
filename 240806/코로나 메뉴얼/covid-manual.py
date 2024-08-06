cnt = 0
for i in range(3):
    a , b = input().split()
    b = int(b)


    if a == 'Y' and b >= 37:
        cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')