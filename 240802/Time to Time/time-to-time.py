def cal_min(h,m):
    return 60*h + m

a,b,c,d = tuple(map(int, input().split()))

print(cal_min(c,d) - cal_min(a,b))