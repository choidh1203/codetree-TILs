arr = list(map(int,input().split()))
cnt = 0
for i in arr:
    if i %3 ==0:
        break
    else:
        cnt = i

print(cnt)