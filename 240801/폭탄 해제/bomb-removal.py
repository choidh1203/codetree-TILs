class bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = input().split()

bomb1 = bomb(code, color, sec)

print(f"""code : {bomb1.code}
color : {bomb1.color}
second : {bomb1.sec}
""")