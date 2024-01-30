a, b = map(int, input().split())
cnt = [0] * b
while a > 1:
    cnt[a%b] += 1
    a = a//b
sum = 0
for i in cnt:
    sum += i**2
print(sum)