n = int(input())
a = n+1
b = 0


for i in range(1,n+1):
    if i %2 == 1:
        a -= 1
        print('* '*a)
        
    else:
        b += 1
        print('* '*b)
        
for i in range(1,n+1):
    if i %2 == 1:
        print('* '*a)
        a += 1
        
    else:
        print('* '*b)
        b -= 1