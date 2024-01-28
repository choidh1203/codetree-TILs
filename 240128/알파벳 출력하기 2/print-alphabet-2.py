n = int(input())
cnt = 65

for i in range(n):
    for j in range(n):
        if i <= j:
            print(chr(cnt),end=" ")
            cnt += 1
            if cnt > ord("Z"):
                cnt = 65
        else:
            print(" ", end =" ")
    print()