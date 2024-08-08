import sys

n = int(input())
arr = list(map(int,input().split()))



min_sum = sys.maxsize

for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += abs(i-j)*arr[j]

    min_sum = min(sum_dist,min_sum)

print(min_sum)