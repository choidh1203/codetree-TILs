start, end = map(int, input().split())
cnt = 0

for i in range(start,end+1):
    li = []
    
    for j in range(1,i):
        if i % j == 0:
            li.append(j)
    if len(li) == 3:
        cnt += 1

print(cnt)