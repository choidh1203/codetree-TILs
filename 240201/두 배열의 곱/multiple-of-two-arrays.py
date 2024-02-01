arr = [list(map(int,input().split())) for _ in range(3)]
a = input()
li = [list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        p = arr[i][j] * li[i][j]
        print(p,end=" ")
    print()