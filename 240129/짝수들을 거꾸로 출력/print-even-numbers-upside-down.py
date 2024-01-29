n = int(input())
arr = list(map(int,input().split()))
li = []
for i in range(n):
    if arr[i]%2 == 0:
        li.append(arr[i])
    else:
        pass
li.reverse()
for i in li:
    print(i, end =" ")