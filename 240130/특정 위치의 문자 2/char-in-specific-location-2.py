arr = list(map(int,input().split()))

for i in range(len(arr)):
    if i == 1 or i == 4 or i == 8:
        print(arr[i], end = " ")