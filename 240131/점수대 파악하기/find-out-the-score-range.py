arr = list(map(int,input().split()))
new = []
for i in arr:
    if i == 0:
        break
    else:
        new.append(i//10)
cnt = [0] * 11

for i in new:
    cnt[i] += 1

for i in range(10,0,-1):
    print(f"{i*10} - {cnt[i]}")