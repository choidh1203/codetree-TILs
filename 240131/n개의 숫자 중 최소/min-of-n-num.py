n = int(input())
arr = list(map(int,input().split()))
arr.sort()
print(arr[0], arr.count(arr[0]))