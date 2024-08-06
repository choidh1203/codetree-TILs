n, t = map(int,input().split())

arr = list(map(int,input().split()))

log =[]
cnt = 0

for i in range(n):
    if arr[i] > t:
        cnt += 1
        log.append(cnt)
    else:
        log.append(cnt)
        cnt = 0

print(0 if max(log) == 0 else max(log))