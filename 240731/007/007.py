code, loc, time = tuple(input().split())

class spy:
    def __init__(self, code, loc, time):
        self.code = code
        self.loc = loc
        self.time = time

a = spy(code, loc, time)

print(f"""secret code : {code}
meeting point : {loc}
time : {time}
""")