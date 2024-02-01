arr = list(map(int,input().split()))
over = []
under = []

for i in arr:
    if i > 500:
        over.append(i)
    elif i < 500:
        under.append(i)

print(max(under), min(over))