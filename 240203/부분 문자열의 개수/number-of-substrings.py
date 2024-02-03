a = input()
b = input()

cnt = 0
for i in range(len(a)-1):
    if b == a[i:i+2]:
        cnt += 1

print(cnt)