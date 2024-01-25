a, b = map(int, input().split())
s = a
while True:
    if s % 2 == 0:
        print(s, end = " ")
    
    if s == b:
        break
    s -= 1