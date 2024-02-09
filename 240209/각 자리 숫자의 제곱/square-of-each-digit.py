def sum(n):
    if n < 10:
        return n**2
    return sum(n//10) + (n%10)**2
n = int(input())
print(sum(n))