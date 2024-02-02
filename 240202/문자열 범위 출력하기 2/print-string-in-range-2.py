n = input()

a = int(input())

if a < len(n):
    for i in range(len(n)-1,len(n)-1 - a, -1):
        print(i,end="")
else:
    for i in range(len(n)-1, -1,-1):
        print(i, end="")