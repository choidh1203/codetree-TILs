a = input()

b = list(a)

for i in range(len(b)):
    if b[i] == a[0]:
        b[i] = a[1]
    elif b[i] == a[1]:
        b[i] = a[0]

print("".join(b))