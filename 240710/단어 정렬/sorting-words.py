n = int(input())
li = [input() for i in range(n)]

li.sort()

for word in li:
    print(word)