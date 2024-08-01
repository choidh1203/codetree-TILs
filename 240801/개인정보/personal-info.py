class person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []

for _ in range(5):
    name, height, weight = tuple(input().split())
    people.append(person(name,int(height),float(weight)))

people.sort(key = lambda x: x.name)

print("name")
for human in people:
    print(f"{human.name} {human.height} {human.weight:.1f}")
print()

people.sort(key = lambda x: -x.height)
print("height")
for human in people:
    print(f"{human.name} {human.height} {human.weight:.1f}")