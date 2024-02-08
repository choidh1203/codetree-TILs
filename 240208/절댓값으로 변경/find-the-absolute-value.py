def a(n):
    arr = list(map(int,input().split()))
    new=[]
    for i in arr:
        s = abs(i)
        new.append(s)
    
    for i in range(n):
        print(new[i], end =" ")

n = int(input())

a(n)