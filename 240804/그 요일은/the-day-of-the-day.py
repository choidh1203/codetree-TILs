num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1,d1,m2,d2 = tuple(map(int,input().split()))

a = input()

cnt = 0

while True:
    if m1 == m2 and d1 == d2:
        break

    cnt += 1
    d1 += 1

    if d1 == num_of_days[m1]:
        d1 = 0
        m1 += 1

if cnt % 7 < days.index(a):
    ans = (cnt // 7)
else:
    ans = (cnt // 7) + 1 

print(ans)