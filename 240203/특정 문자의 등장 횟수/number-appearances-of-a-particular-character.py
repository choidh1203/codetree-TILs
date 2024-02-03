a = input()
cnt1 = 0
cnt2 = 0
for i in range(len(a)-1):
    if 'ee' == a[i:i+2]:
        cnt1 += 1
    if 'eb' == a[i:i+2]:
        cnt2 += 1
print(cnt1, cnt2)