n = int(input())

new = [0]*(n+1)

max_num = max(new)

arr = list(map(int,input().split()))

new = [0]*(max_num+1)

for i in arr:
    new[i] += 1

new2 = []

for i in range(max_num + 1):
    if new[i] == 1:
        new2.append(i)
if new2:
    print(max(new2))
else:
    print(-1)