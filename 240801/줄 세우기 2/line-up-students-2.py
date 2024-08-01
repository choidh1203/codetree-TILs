class student:
    def __init__(self, h, w, idx):
        self.h, self.w, self.idx = h, w, idx

n = int(input())

students = []

for i in range(1,n+1):
    h, w = map(int,input().split())
    students.append(student(h,w,i))

students.sort(key = lambda x: (x.h,-x.w))

for student in students:
    print(f"{student.h} {student.w} {student.idx}")