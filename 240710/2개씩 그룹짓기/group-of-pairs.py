n = int(input())
numbers = list(map(int, input().split()))

fin = []

numbers.sort()
for i in range(n):
    fin.append(numbers[i] + numbers[2*n-1-i])

print(max(fin))