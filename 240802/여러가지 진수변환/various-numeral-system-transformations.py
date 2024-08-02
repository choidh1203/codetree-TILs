n, b = tuple(map(int, input().split()))

numbers = []
while n > b:
    numbers.append(n%b)
    n //= b
    
numbers.append(n)
for number in numbers[::-1]:
    print(number, end="")