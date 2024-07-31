class student:
    def __init__(self, h, w, i):
        self.h = h
        self.w = w
        self.i = i

n = int(input())
students = []

for i in range(1,n+1):
    h, w = tuple(map(int, input().split()))
    students.append(student(h,w,i))

students.sort(key = lambda x: (-x.h,-x.w,x.i))

for student in students:
    print(student.h, student.w, student.i)