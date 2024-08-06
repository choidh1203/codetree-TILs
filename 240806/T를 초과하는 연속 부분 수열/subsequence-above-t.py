n, t = map(int,input().split())

arr = list(map(int,input().split()))

log =[]
cnt = 0

for i in range(n):
    if arr[i] > 3:
        if i == 0 or arr[i-1] < arr[i]:
            cnt += 1
            log.append(cnt)
        else:
            log.append(cnt)
            cnt = 1
    else:
        log. append(cnt)
        cnt = 0

print(0 if max(log) == 1 else max(log))