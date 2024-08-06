n, m = map(int,input().split())

log_a = [0]
log_b = [0]

ax = 0
bx = 0

for i in range(n):
    d, t = input().split()
    t = int(t)
    
    for j in range(t):
        if d == 'R':
            ax += 1
        else:
            ax -= 1

        log_a.append(ax)

for i in range(m):
    d, t = input().split()
    t = int(t)
    
    for j in range(t):
        if d == 'R':
            bx += 1
        else:
            bx -= 1

        log_b.append(bx)

idx = 0

for k in range(1,len(log_a)):
    if log_a[k] == log_b[k]:
        idx  = k
        break

print(-1 if idx == 0 else idx)