string = input()

char = [string[0]]
idx = [1]

for i in range(1,len(string)):
    if string[i] == string[i-1]:
        idx[-1] += 1
    else:
        char.append(string[i])
        idx.append(1)

print(len(char)+len(''.join(str(e) for e in char)))

for i in range(len(char)):
    print(char[i]+str(idx[i]),end="")