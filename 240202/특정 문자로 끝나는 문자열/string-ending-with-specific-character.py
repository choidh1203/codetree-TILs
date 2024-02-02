arr =[]
for i in range(10):
    arr.append(input())

a = input()
cnt = 0
for word in arr:
    if word[-1] == a:
        print(word)
        cnt += 1

if cnt == 0:
    print('None')