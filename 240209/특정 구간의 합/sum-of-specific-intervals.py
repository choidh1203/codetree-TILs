def gang():
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(m):
        sum = 0
        a1, a2 = map(int,input().split())
        for j in range(a2-a1+1):
            sum += a[a1-1+j]
        print(sum)

gang()