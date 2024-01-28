n = int(input())

for i in range(1,n+1):
    li = []
    
    for j in range(1,i+1):
        if i % j == 0:
            li.append(j)
    if len(li) == 2:
        print(i, end =" ")