n = int(input())
arr= []
for i in range(n):
    arr.append(input())

a = input()
cnt = 0
num = 0

for word in arr:
    if word[0] == a:
        cnt += 1
        num += len(word)

print(cnt, "{0:.2f}".format(num/cnt))