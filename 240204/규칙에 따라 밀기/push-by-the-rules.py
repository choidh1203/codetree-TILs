a = input()
o = input()

for i in o:
    if i == 'L':
        a = a[1:] + a[0]
    if i == 'R':
        a = a[-1] + a[0:-1]

print(a)