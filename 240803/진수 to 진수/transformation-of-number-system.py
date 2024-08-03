a, b = tuple(map(int, input().split()))

n = input()

#십진수 만들기
num = 0

for i in n:
    num = num*a + int(i)


digits = []
#b진수 만들기
while num>=b:
    digits.append(num%b)
    num //= b


digits.append(num)

for digit in digits[::-1]:
    print(digit, end="")