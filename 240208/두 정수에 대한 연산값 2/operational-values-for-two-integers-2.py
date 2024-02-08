def gang(a,b):
    if max(a,b) == a:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    print(a,b)

a,b = map(int,input().split())

gang(a,b)