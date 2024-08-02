a, b, c = tuple(map(int,input().split()))

d = 11
h = 11
m = 11

ans = 0

while True:
    if a < d and b < h and c < m:
        ans = -1
        break

    if d == a and h == b and m == c:
        break

    m+= 1
    ans += 1

    if m == 60:
        h += 1
        m = 0
    
    if h == 24:
        d += 1
        h = 0
    
print(ans)