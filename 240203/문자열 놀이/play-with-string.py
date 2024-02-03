s, q = input().split()

for i in range(int(q)):
    n, a, b = input().split()
    n = int(n)
    if n == 1:
        a = int(a)
        b = int(b)
        new = list(s)
        new[a-1] = s[b-1]
        new[b-1] = s[a-1]
        s = "".join(new)
        print(s)
    elif n == 2:
        s = s.replace(a,b)
        print(s)