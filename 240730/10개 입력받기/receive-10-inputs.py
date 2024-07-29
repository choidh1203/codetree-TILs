arr = list(map(int,input().split()))
sum = 0
cnt = 0
for i in arr:
    if i !=0:
        sum += i
        cnt += 1
    else:
        break

print(sum, "{0:.1f}".format(sum/cnt))