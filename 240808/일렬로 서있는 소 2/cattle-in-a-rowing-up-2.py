n = int(input())

cows = list(map(int,input().split()))

ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cows[i] <= cows[j] <= cows[k]:
                ans += 1

print(ans)