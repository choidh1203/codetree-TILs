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
    if len(numbers) == 2:
        return lcm(numbers[0], numbers[1])
    else:
        return lcm(numbers[0], expanded_lcm(numbers[1:]))

print(expanded_lcm(b))