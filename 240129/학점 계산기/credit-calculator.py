n = int(input())

arr = list(map(float, input().split()))
sum = 0

for i in range(n):
    sum += arr[i]
print("{:.1f}".format(sum/n))
if sum/n > 4.0:
    print('Perfect')
elif sum/n > 3.0:
    print('Good')
else:
    print('Poor')