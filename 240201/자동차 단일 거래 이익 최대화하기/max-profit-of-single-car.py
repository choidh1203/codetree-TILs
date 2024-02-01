n = int(input())

arr = list(map(int,input().split()))
profit = 0
for i in range(n):
    for j in range(n):
        if i <= j:
            if profit < arr[j] - arr[i]:
                profit = arr[j] - arr[i]

if profit > 0:
    print(profit)
else:
    print(0)