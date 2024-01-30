n1, n2 = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

li = [0]*n1

cnt = 1
cnt2 = 0
if a.count(b[0]) == 1:
    start = a.index(b[0])
    for i in range(1,n2):
        if b[i] == a[start+i]:
            cnt += 1

    if cnt == len(b):
        print("Yes")
    else:
        print("No")
elif a.count(b[0]) > 1:
    for i in range(n1):
        if b[0] == a[i]:
            li[i] += 1
    for j in li:
        if j == 1:
            for i in range(1,n2):
                if b[i] == a[start+i]:
                    cnt += 1
                if cnt == len(b):
                    cnt2 += 1
            if cnt2 >= 1:
                print("Yes")
            else:
                print("No")
else:
    print('No')