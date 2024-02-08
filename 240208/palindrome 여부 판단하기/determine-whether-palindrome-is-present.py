def idn(s):
    s = list(s)
    a = s[::-1]
    if s == a:
        print('Yes')
    else:
        print('No')

s = input()
idn(s)