string, char = input().split()

if char in string:
    print(string.find(char))
else:
    print("No")