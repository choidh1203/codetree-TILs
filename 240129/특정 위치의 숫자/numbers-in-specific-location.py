a = list(map(int, input().split()))
b = 0

for i in range(1,11):
    if i == 3 or i == 5 or i ==10:
        b += a[i-1]
print(b)