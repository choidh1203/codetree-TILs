a, b, c = map(int,input().split())

def hap(n):
    if n < 10:
        return n
    
    return hap(n//10) + n % 10

print(hap(a*b*c))