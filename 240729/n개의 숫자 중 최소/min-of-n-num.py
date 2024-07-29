import sys

n = int(input())
arr = list(map(int, input().split()))

min_val = sys.maxsize

cnt = 0

for i in range(n):
    if min_val > arr[i]:
        min_val = arr[i]
        cnt = 1
    elif min_val == arr[i]:
        cnt += 1

print(min_val, cnt)