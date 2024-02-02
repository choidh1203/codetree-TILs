n = int(input())

l = 0
a = 0

for i in range(n):
    m = input()
    l += len(m)
    if m[0] == a:
        a += 1

print(l, a)