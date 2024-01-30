n, q = map(int,input().split())

arr = list(map(int,input().split()))

for i in range(q):
    li = list(map(int,input().split()))
    if li[0] == 1:
        print(arr[li[1]-1])
    elif li[0] == 2:
        if li[1] in arr:
            print(arr.index(li[1])+1)
        else:
            print(0)
    elif li[0] == 3:
        for j in range(li[1]-1,li[2]):
            print(arr[j],end =" ")
        print()