class point:
    def __init__(self,x, y,idx):
        self.x = x
        self.y = y
        self.idx = idx

n = int(input())

points = []

for i in range(1,n+1):
    x, y = tuple(input().split())
    points.append(point(int(x),int(y),i))

points.sort(key = lambda p: (abs(p.x)+abs(p.y),p.idx))

for point in points:
    print(point.idx)