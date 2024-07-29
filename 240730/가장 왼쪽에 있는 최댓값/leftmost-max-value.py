n = int(input())
arr= list(map(int,input().split()))

while True:
    a = arr.index(max(arr))
    arr = arr[0:a]
    print(a+1, end =" ")
    if a == 0:
        break