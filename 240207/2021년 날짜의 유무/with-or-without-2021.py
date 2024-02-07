def date(m,d):
    if 1<= m <= 12:
        if m == 2:
            if 1<= d <= 28:
                print('Yes')
            else:
                print('No')
        elif m%2 == 0:
            if 1<= d <= 30:
                print('Yes')
            else:
                print('No')
        else:
            if 1<= d <= 31:
                print('Yes')
            else:
                print('No')
    else:
        print('No')

m,d = map(int, input().split())

date(m,d)