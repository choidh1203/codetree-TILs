cnt = 1

n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print(cnt, end = " ")
        cnt += 1
    print()