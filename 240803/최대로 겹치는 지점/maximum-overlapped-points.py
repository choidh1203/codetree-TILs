arr = [0]*101

n= int(input())

for i in range(n):
    x1, x2 = tuple(map(int,input().split()))

    for x in range(x1, x2+1):
        arr[x] += 1

print(max(arr))