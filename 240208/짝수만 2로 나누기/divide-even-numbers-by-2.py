def mod(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = int(arr[i]/2)
n = int(input())
arr = list(map(int,input().split()))

mod(arr)


for elem in arr:
    print(elem, end = " ")