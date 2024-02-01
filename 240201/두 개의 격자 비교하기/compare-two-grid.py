n, m = map(int,input().split())
arr = [
    list(map(int,input().split())) 
    for _ in range(n)
    ]
li = [
    list(map(int,input().split())) 
    for _ in range(n)
    ]
new = [
    [0 for _ in range(m)] 
    for _ in range(n)
    ]

for i in range(n):
    for j in range(m):
        if arr[i][j] == li[i][j]:
            new[i][j] = 0
        else:
            new[i][j] = 1

for row in new:
    for elem in row:
        print(elem,end = " ")
    print()