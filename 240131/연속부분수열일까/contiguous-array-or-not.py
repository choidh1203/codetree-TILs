n1, n2 = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

check = False

for i in range(n1 - n2 + 1):
    if a[i:i+n2] == b:
        check =True
        break
if check:
    print("Yes")
else:
    print("No")