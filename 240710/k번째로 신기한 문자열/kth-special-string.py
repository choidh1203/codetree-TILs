n, k, t = input().split()
n = int(n)
k = int(k)

words = [input() for i in range(n)]

fin = []

for word in words:
    if t in word:
        fin.append(word)
    else:
        pass

fin.sort()

print(fin[k-1])