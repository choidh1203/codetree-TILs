class person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

n = int(input())

people=[]

for _ in range(n):
    name, h, w = tuple(input().split())
    people.append(person(name, int(h), int(w)))

people.sort(key = lambda x: (x.h, -x.w))

for person in people:
    print(f"{person.name} {person.h} {person.w}")