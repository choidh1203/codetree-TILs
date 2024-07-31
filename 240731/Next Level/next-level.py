class user:
    def __init__(self, id, lv):
        self.id = id
        self.lv = lv
    def print_format(self):
        print(f"user {self.id} lv {self.lv}")

user1 = user("codetree", "10")
user2 = user("codetree", "10")

id, lv = tuple(input().split())

user2.id = id
user2.lv = lv

user1.print_format()
user2.print_format()