start, end = map(int, input().split())
cnt = 0

for i in range(start,end+1):
    li = []
    sum = 0
    
    for j in range(1,i):
        if i % j == 0:
            li.append(j)
    
    for x in li:
        sum += x
    
    if sum == i:
        cnt += 1

print(cnt)