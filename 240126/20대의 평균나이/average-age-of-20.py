avg = 0
n = 0

while True:
    a = int(input())
    if a in range(20,30):
        avg += a
        n += 1
    else:
        break

avg = avg/n
print("{0:.2f}.format(avg)")