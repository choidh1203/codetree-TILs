n = int(input())
cnt = 0


for i in range(1,n+1):
    if i%2 == 1:
        for j in range(1, n+1):
            cnt += 1
            print(cnt, end = " ")
            
        print()
    else:
        for j in range(1,n+1):
            cnt += 2
            print(cnt, end =" ")
            
        print()