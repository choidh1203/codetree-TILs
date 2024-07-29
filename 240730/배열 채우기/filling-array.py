arr = list(map(int,input().split()))
li = []
for i in arr:
    if i !=0:
        li.append(i)
    else:
        break
li.reverse()

for i in li:
    print(i, end = " ")