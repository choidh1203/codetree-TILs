a = int(input())
b = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return abs(a*b)//gcd(a, b)

def expanded_lcm(numbers):
    fin_lcm = numbers[0]
    for i in numbers[1:]:
        fin_lcm = lcm(fin_lcm, i)
    return fin_lcm

print(expanded_lcm(b))