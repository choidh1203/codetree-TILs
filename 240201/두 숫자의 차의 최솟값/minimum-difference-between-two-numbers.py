n = int(input())
arr = list(map(int,input().split()))

profit = 10
for i in range(0,n-1):
    if profit > arr[i+1] - arr[i]:
        profit = arr[i+1] - arr[i]
print(profit)