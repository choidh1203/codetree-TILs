a,b,c,d = tuple(map(int, input().split()))

ans = 0
while True:
    if a == c and b == d:
        break
    ans+=1
    b+=1
    if b == 60:
        a += 1
        b = 0

print(ans)