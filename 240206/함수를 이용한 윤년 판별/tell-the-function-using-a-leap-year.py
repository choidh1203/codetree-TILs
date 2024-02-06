def year(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                print('true')
            else:
                print('false')
        else:
            print('true')
    else:
        print('false')

y = int(input())

year(y)