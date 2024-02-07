def add(a,b):
    print(f"{a} + {b} = {a+b}")
def minus(a,b):
    print(f"{a} - {b} = {a-b}")
def times(a,b):
    print(f"{a} * {b} = {a*b}")
def divide(a,b):
    print(f"{a} / {b} = {a//b}")
def main(a,b):
    if '+' == o:
        add(a,b)
    elif '-' == o:
        minus(a,b)
    elif '*' == o:
        times(a,b)
    elif '/' == o:
        divide(a,b)
    else:
        print('False')

a,o,c = map(str,input().split())
a = int(a) ; c = int(c)
main(a,c)