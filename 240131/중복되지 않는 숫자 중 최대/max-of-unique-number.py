n = int(input())

new = [0]*(n+1)

arr = list(map(int,input().split()))

for i in arr:
    new[i] += 1

new2 =[]
for i in range(n+1):
    if new[i] == 1:
        new2.append(i)
print(max(new2))