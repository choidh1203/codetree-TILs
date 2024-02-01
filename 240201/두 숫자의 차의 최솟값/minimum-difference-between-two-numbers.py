n = int(input())
arr = list(map(int,input().split()))

profit = 10
for i in range(n):
    for j in range(n):
        if i !=j:
            if profit > abs(arr[j] - arr[i]):
                profit = abs(arr[j] - arr[i])
print(profit)