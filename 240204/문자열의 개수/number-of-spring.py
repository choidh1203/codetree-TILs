notZero = True
cnt = 0
even = []
while notZero:
    string = input()
    if string == '0':
        notZero = False
        continue
    cnt+=1
    if cnt %2 == 1:
        even.append(string)

print(cnt)
for i in even:
    print(i)