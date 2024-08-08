n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(n-2):
        cnt = 0
        for dj in range(3):
            if arr[i][j+dj] == 1:
                    cnt +=1
        ans = max(ans, cnt)

print(ans)