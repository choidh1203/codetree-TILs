arr = list(map(int, input().split()))

# 3번째 항부터 10번째 항까지 추가
for i in range(2, 10): 
    arr.append((arr[-1] + arr[-2]))


for i in arr:
    print(i%10, end = " ")