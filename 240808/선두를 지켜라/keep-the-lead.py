n,m = map(int,input().split())

alog = [0]
blog = [0]

for _ in range(n):
    v1,t1 = map(int,input().split())
    for i in range(t1):
        alog.append(v1+alog[-1])

for _ in range(m):
    v2, t2  = map(int,input().split())
    for j in range(t2):    
        blog.append(v2+blog[-1])

cnt = 0
rank = []


for k in range(1,len(alog)):
    if alog[k] > blog[k]:
        rank.append(1)
    elif alog[k] < blog[k]:
        rank.append(2)
    else:
        rank.append(rank[-1])

for l in range(1,len(rank)):
    if rank[l] != rank[l-1]:
        cnt += 1

print(cnt)