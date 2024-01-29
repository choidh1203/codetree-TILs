arr = list(map(int, input().split()))

n = len(arr)

sum = 0
cnt = 0
cb = 0
for i in range(0,n):
    if i  % 2 == 1:
        sum += arr[i]
    if i % 3 == 2:
        cnt += arr[i]
        cb += 1
print(sum, "{0:.1f}".format(cnt/cb))