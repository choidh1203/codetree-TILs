n = int(input())

gang = [0] * 200

lines = [list(map(int,input().split())) for i in range(n)]

for line in lines:
    for i in range(line[0]+100,line[1]+100):
        gang[i] += 1    
print(max(gang))