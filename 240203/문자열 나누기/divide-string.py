n = int(input())

arr = input().split()

arr = "".join(arr)

for i in range(len(arr)):
    if i % 5 == 4:
        print(arr[i])
        
    else:
        print(arr[i],end="")