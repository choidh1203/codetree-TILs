arr = [list(map(int,input().split())) for _ in range(2)]

point = 0
for i in range(2):
    print("{:.1f}".format(sum(arr[i])/4),end =" ")
print()

for i in range(4):
    avg = 0
    for j in range(2):
        avg += arr[j][i]
    print("{:.1f}".format(avg/2),end =" ")
print()

for i in range(2):
    for j in range(4):
        point += arr[i][j]
print("{:.1f}".format(point/8))