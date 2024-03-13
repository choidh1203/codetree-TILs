a = int(input())
cnt = 0

def su(n):
    global cnt
    if n == 1:
        return cnt

    cnt += 1

    if n % 2 == 0:
        return su(n/2)
    else:
        return su(3*n+1)

print(su(a))