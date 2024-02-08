def yoon(y):
    if y % 4 == 0:
        if y%100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def exist(m,d):
    if yoon(y):
        if m == 2:
            if 1 <= d <= 29:
                return True
            else:
                return False
        elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m ==12:
            if 1<= d <= 31:
                return True
            else:
                return False
        else:
            if 1<=d <= 30:
                return True
            else:
                return False
    else:
        if m == 2:
            if 1 <= d <= 28:
                return True
            else:
                return False
        elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m ==12:
            if 1<= d <= 31:
                return True
            else:
                return False
        else:
            if 1<=d <= 30:
                return True
            else:
                return False

def main(y,m,d):
    if exist(m,d):
        if 3<= m <= 5:
            print('Spring')
        elif 6<= m <= 8:
            print('Summer')
        elif 9 <= m <= 11:
            print('Fall')
        elif m == 12 or 1<=m<= 2:
            print('Winter')
    else:
        print(-1)

y,m,d = map(int,input().split())

main(y,m,d)