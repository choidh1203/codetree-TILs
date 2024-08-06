n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0
log = []

for i in range(n):
    if i == 0 or arr[i-1] == arr[i]:
        cnt += 1
    if arr[i-1] != arr[i]:
        log.append(cnt)
        cnt = 1

print(max(log))