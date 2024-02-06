def min_num(n,m):
    for i in range(max(n,m), n*m+1):
        if i % n == 0 and i % m == 0:
            a = i 
            break
    print(a)

n,m = map(int,input().split())

min_num(n,m)