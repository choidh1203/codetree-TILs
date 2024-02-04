n = int(input())
sum = 0
for i in range(n):
    a = int(input())
    sum += a
sum = str(sum)

o = sum[1:]+sum[0]
print(o)