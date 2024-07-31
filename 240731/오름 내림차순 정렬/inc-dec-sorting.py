n = int(input())
numbers = list(map(int,input().split()))

#리스트 정렬
asc_numbers = sorted(numbers)
desc_numbers = asc_numbers[::-1]

#정렬된 리스트 출력
for num in asc_numbers:
    print(num, end=" ")
print()

for num in desc_numbers:
    print(num, end=" ")