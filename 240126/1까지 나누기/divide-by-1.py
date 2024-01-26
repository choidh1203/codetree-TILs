n = int(input())
d = 1

while True:
    if n//d <= 1:
        break
    n = n//d
    d += 1
    

print(d)