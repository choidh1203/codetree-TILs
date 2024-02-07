n1, n2 = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

def idn(a, b):
    for i in range(n1 - n2 + 1):
        if b == a[i:i+n2]:
            return 'Yes'
    return 'No'
    
print(idn(a,b))