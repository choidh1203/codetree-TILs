r, c = map(int,input().split())
arr = [list(input().split()) for _ in range(r)]

cnt = 0

for i in range(1,r):
    for j in range(1,c):
        for k in range(i+1, r-1):
            for l in range(j+1, c-1):
                s1 = arr[i][j]
                s2 = arr[k][l]
                if arr[0][0] != s1 and s1 != s2 and s2 != arr[r-1][c-1]:
                    cnt += 1

print(cnt)