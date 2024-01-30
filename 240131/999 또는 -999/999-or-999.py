arr = list(map(int,input().split()))

new = []

for i in arr:
    if i == 999 or i == -999:
        break
    else:
        new.append(i)

print(max(new), min(new))