arr = input().split()
sum = 0
cnt = 0
for i in arr:
    if int(i) < 250:
        sum += int(i)
        cnt += 1
    else:
        break
print(sum, "{:.1f}".format(sum/cnt))