arr = list(map(int,input().split()))

if 0 in arr:
    arr.remove(0)

arr.reverse()

for i in arr:
    print(i,end = " ")