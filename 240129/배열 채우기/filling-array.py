li = []
for i in range(10):
    n = int(input())
    if n != 0:
        li.append(n)
    else:
        break

li.reverse()
for i in li:
    print(i, end =" ")