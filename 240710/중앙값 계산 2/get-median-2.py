n = int(input())
numbers = list(map(int,input().split()))

fin = []

for i in range(n):
    fin.append(numbers[i])
    fin.sort()
    if i%2 == 0:
        mid = fin[int(i/2)]
        print(mid, end = " ")