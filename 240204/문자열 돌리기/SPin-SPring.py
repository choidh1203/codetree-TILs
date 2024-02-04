s = input()
l = len(s)

for i in range(0,l+1):
    if i == 0:
        print(s)
    else:
        o = s[-i:]+s[0:-i]
        print(o)