def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def even(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 2 == 0:
        return True
    else:
        return False

def main(a,b):
    cnt = 0
    for i in range(a,b+1):
        if prime(i) and even(i):
            cnt += 1
        else:
            pass
    print(cnt)

a,b = map(int, input().split())
main(a,b)