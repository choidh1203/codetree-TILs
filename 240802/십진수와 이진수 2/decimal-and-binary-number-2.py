n = list(input())

#십진수 만들기
num = 0

for i in n:
    num = num*2 + int(i)

num *= 17
digits = []
#이진수 만들기
while num>1:
    digits.append(num%2)
    num //= 2


digits.append(num)

for digit in digits[::-1]:
    print(digit, end="")