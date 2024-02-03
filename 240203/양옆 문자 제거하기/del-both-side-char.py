s = list(input())

s.pop(s[1])
s.pop(s[-2])
print("".join(s))