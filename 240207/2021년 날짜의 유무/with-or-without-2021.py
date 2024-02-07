def date(m,d):
    if 1<= m <= 12:
        if m == 2:
            if 1<= d <= 28:
                print('Yes')
            else:
                print('No')
        elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if 1<= d <= 31:
                print('Yes')
            else:
                print('No')
        else:
            if 1<= d <= 30:
                print('Yes')
            else:
                print('No')
    else:
        print('No')

m,d = map(int, input().split())

date(m,d)