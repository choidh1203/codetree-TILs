n = int(input())
cnt1 = 1
cnt2 = 2*n
for i in range(1,n+1):
    if i%2 == 1:
        for j in range(n):
            print(cnt1,end = " ")
            cnt1 += 1
        cnt1 += n
        print()
    else:
        for j in range(n):
            print(cnt2, end = " ")
            cnt2 -= 1
        cnt2 += 3*n
        print()