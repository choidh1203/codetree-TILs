n = int(input())
cnt = 0
for i in range(n):
    cnt +=1
    print("*"*cnt)
    print()
    
for i in range(n-1):
    cnt -=1
    print("*"*cnt)
    print()