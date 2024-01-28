m = int(input())

for i in range(m):
    sum = 0
    n = int(input())
    while n != 1:
        sum += 1
        if n%2 == 1:
            n = 3*n+1
        else:
            n = n/2
    print(sum)