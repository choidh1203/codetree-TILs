a, b = input().split()

c=""
d=""

for i in a:
    if i >= '0' and i <= '9':
        c += i
    else:
        break
for i in b:
    if i >= '0' and i <= '9':
        d += i
    else:
        break

print(int(c)+int(d))