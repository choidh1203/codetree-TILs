n = int(input())
cnt = 0
for i in range(n):
    sum = 0
    
    arr = list(map(int,input().split()))
    for j in arr:
        sum += j
    if sum/4 >= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')
print(cnt)