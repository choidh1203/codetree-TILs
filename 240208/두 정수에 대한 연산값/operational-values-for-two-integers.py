def gang(a, b):
    if max(a,b) == a:
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    print(a,b)


a, b = map(int, input().split())
gang(a, b)