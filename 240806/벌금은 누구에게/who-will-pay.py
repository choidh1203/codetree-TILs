n, m, k = map(int,input().split())

students = [0 for _ in range(n+1)]

for i in range(m):
    if max(students) == k:
        print(students.index(max(students)))
        break
    b = int(input())
    students[b] += 1