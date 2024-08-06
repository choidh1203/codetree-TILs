n = int(input())

arr = [int(input()) for _ in range(n)]

log = []

cnt = 0

for i in range(n):
    if i == 0 or (arr[i-1] < 0 and arr[i] < 0) or (arr[i-1] > 0 and arr[i] > 0):
        cnt += 1
        log.append(cnt)
    else:
        log.append(cnt)
        cnt = 1

print(max(log))