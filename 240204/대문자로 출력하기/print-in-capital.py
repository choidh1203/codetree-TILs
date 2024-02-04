arr = input()

for i in arr:
    if i >= 'A' and i <= 'Z':
        print(i,end="")
    elif i >= 'a' and i <= 'z':
        print(i.upper(),end="")