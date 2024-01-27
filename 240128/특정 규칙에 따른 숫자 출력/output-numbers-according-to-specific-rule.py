cnt = 1
n = int(input())
for i in range(n):
    for j in range(n):
        if j <= i:
            print(cnt, end =" ")
        else:
            print(" ", end = " ")
    print()