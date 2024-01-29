n = int(input())

arr = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum += arr[i]
print("{:.1f}".format(sum/n))
if sum > 4.0:
    print('Perfect')
elif sum > 3.0:
    print('Good')
else:
    print('Poor')