def two(a):
    new = []
    for char in a:
        if not char in new:
            new.append(char)
        else:
            pass
    if len(new) >= 2:
        print('Yes')
    else:
        print('No')

a = input()

two(a)