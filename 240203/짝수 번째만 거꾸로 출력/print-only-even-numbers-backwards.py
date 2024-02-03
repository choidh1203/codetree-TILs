string = input()

new_str = []

for i in range(len(string)):
    if i % 2 == 1:
        new_str.append(string[i])

for i in range(len(new_str)-1, -1 , -1):
    print(new_str[i],end="")