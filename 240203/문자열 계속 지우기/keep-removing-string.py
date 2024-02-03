a = list(input())
b = list(input())

exist = True

while exist:
    for i in range(len(a)-len(b)+1):
        if b == a[i:i+len(b)]:
            del a[i:i+len(b)]
    if not "".join(b) in "".join(a):
        exist = False

print("".join(a))