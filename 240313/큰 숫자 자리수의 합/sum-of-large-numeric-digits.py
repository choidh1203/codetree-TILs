a = list(map(int,input().split()))
hap = 1
for num in a:
    hap *= num
hap = str(hap)
_len = len(hap)

def num_hap(n):
    if n == _len-1:
        return int(hap[n])

    return int(hap[n]) + num_hap(n+1) 

print(num_hap(0))