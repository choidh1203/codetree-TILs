class person:
    def __init__(self, name, addy, city):
        self.name = name
        self.addy = addy
        self.city = city

n = int(input())
people = []

for _ in range(n):
    name, addy, city = tuple(input().split())
    people.append(person(name,addy,city))

people.sort(key = lambda x: x.name, reverse = True)

print(f"""name {people[0].name}
addr {people[0].addy}
city {people[0].city}
""")