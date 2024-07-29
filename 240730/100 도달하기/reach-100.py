n = int(input())
cnt = 2
arr = [1, n]

while arr[-1] <= 100:
    arr.append(arr[cnt-1] + arr[cnt-2])
    cnt += 1

for i in arr:
    print(i, end =" ")