a = int(input())
b = int(input())

if a == 0 and b >= 19:
    print('MAN')
elif a == 0 and b < 19:
    print('BOY')
elif a == 1 and b >= 19:
    print('WOMAN')
else:
    print('GIRL')