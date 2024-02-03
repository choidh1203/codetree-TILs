s = list(input())

for i in range(len(s)-1):
    n = int(input())
    if len(s) < n-1:
        s.pop(-1)
    else:
        s.pop(n)

    print("".join(s))