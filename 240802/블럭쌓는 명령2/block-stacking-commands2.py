n, k = tuple(map(int,input().split()))

block = [0] * (n+1)

intervals = [list(map(int,input().split())) for _ in range(k)]

for interval in intervals:
    for i in range(interval[0], interval[1]+1):
        block[i] += 1

print(max(block))