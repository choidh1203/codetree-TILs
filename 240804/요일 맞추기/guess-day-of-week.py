m1, d1, m2, d2 = tuple(map(int,input().split()))

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

cnt = 0

if m1 == m2 and d1 == d2:
    print('Mon')
elif (m1 == m2 and d1 < d2) or m1 < m2:
    while True:
        if m1 == m2 and d1 == d2:
            break
    
        cnt += 1
        d1 += 1

        if d1 == num_of_days[m1]:
            d1 = 0
            m1 += 1

    for i in range(7):
        if cnt % 7 == i:
            print(days[i])
else:
    while True:
        if m1 == m2 and d1 == d2:
            break
        
        cnt += 1
        d1 -= 1

        if d1 == 0:
            d1 = num_of_days[m1-1]
            m1 -= 1
    
    for i in range(7):
        if cnt % 7 == 0:
            print('Mon')
        elif cnt % 7 == 7-i:
            print(days[i])