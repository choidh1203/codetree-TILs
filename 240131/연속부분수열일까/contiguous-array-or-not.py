n1, n2 = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

cnt = 1
if b[0] in a:
    start = a.index(b[0])
    for i in range(1,n2):
        if b[i] == a[start+i]:
            cnt += 1

    if cnt == len(b):
        print("Yes")
    else:
        print("No")
else:
    print('No')