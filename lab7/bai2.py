students = {}
for i in range(1, 11):
    name = input(f"Nhập tên của sinh viên thứ {i}: ")
    score = float(input(f"Nhập điểm thi của sinh viên {name}: "))
    students[name] = score

grades = {}
for name, score in students.items():
    if score < 4.0:
        grades[name] = 'F'
    elif 4.0 <= score < 5.5:
        grades[name] = 'D'
    elif 5.5 <= score < 7.0:
        grades[name] = 'C'
    elif 7.0 <= score < 8.5:
        grades[name] = 'B'
    else:
        grades[name] = 'A'

print("Xếp loại học lực của các sinh viên:")
for name, grade in grades.items():
    print(f"{name}: {grade}")

grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

for grade in grades.values():
    grade_count[grade] += 1

print("Thống kê số lượng sinh viên ở mỗi loại học lực:")
for grade, count in grade_count.items():
    print(f"{grade}: {count}")
