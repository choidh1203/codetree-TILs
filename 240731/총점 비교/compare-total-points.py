class student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.score = kor + eng + math

n = int(input())
students = []

for _ in range(n):
    name, kor, eng, math = tuple(input().split())
    kor, eng, math = int(kor), int(eng), int(math)
    students.append(student(name,kor,eng,math))

students.sort(key = lambda x : x.score)

for student in students:
    print(f"{student.name} {student.kor} {student.eng} {student.math}")