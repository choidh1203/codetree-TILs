n, a = input().split()
cnt =0
for i in range(int(n)):
    b = input()
    if a == b:
        cnt+=1
print(cnt)