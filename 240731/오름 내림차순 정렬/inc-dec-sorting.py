n = int(input())
numbers = list(map(int,input().split()))

asc_numbers = sorted(numbers)
desc_numbers = asc_numbers[::-1]

for num in asc_numbers:
    print(num, end=" ")
print()

for num in desc_numbers:
    print(num, end=" ")