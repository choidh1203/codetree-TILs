arr = list(map(int,input().split()))

new_arr = []

for i in arr:
    if i == 0:
        break
    else:
        new_arr.append(i)
for i in new_arr:
    if i % 2 == 1:
        print(i+3, end =" ")
    else:
        print(i//2, end = " ")