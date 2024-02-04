s, q = input().split()
q = int(q)
s = list(s)
for i in range(q):
    n = int(input())
    if n == 1:
        #왼쪽 로테이트
        s = s[1:]+[s[0]]
        print("".join(s))
    elif n == 2:
        #오른쪽 로테이트
        s = [s[-1]] + s[0:-1]
        print("".join(s))
    elif n == 3:
        #리버스
        s.reverse()
        print("".join(s))