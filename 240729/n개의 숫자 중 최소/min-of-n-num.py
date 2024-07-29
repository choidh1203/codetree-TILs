import sys

n = int(input())
arr = list(map(int, input().split()))

min_val = sys.maxsize

idx = 0

for i in range(n):
    if min_val > arr[i]:
        min_val = arr[i]
        idx = i

print(min_val, idx)