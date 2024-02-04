a = input()
b= input()

c=""
d=""

for i in a:
    if i >= '0' and i <= '9':
        c += i

for i in b:
    if i >= '0' and i <= '9':
        d += i
print(int(c)+int(d))