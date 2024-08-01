class goods:
    def __init__(self,name,code):
        self.name = name
        self.code = code

name, code = input().split()

good1 = goods("codetree","50")
good2 = goods(name, code)

print(f"""product {good1.code} is {good1.name}
product {good2.code} is {good2.name}
""")