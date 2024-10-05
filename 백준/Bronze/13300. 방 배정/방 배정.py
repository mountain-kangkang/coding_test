n, k = map(int, input().split())
students = []
for i in range(n):
    student = list(map(int, input().split()))
    students.append(student)

room = 0
for gender in range(2):
    for grade in range(1, 6 + 1):
        count = 0
        for student in students:
            if student[0] == gender and student[1] == grade:
                count += 1
        room = room + (count // k)
        if count % k:
            room += 1
print(room)