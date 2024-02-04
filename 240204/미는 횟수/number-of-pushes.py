a = input()
b = input()

cnt = 0

while True:
    a = a[-1]+a[0:-1]
    cnt += 1
    if a == b:
        print(cnt)
        break
    if cnt >= len(a):
        print(-1)
        break