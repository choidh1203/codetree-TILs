arr = list(map(int,input().split()))
li = []
for i in arr:
    if i !=0:
        li.append(i)
    else:
        break
sum = 0
for i in range(1,4):
    sum += li[-i]

print(sum)