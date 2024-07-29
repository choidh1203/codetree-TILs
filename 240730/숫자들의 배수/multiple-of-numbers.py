n = int(input())
time = 0
cnt = 0
while cnt != 2:
    time += 1
    print(n*time, end = " ")
    
    if (n * time) % 5 == 0:
        cnt += 1