class student:
    def __init__(self, h, w, idx=0):
        self.h = h
        self.w = w
        self.idx = 0

n = int(input())
students = []

for _ in range(n):
    h, w = tuple(map(int, input().split()))
    students.append(student(h,w))

for idx, student in enumerate(students, start = 1):
    student.idx = idx

students.sort(key = lambda x: (-x.h,-x.w,x.idx))

for student in students:
    print(student.h, student.w, student.idx)