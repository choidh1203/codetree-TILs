def prime_map(n):
    for j in range(2, n):
        if n % j == 0:
            return False
    return True
        

def main(start, end):
    prime_sum = 0
    for i in range(start, end+1):
        if prime_map(i):
            prime_sum += i
    print(prime_sum)

a, b = map(int,input().split())

main(a,b)