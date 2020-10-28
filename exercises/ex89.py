all_students = []
student = []
grades = []

while True:
    name = str(input("Type the student name: "))
    if name == "exit":
        break
    grade1 = float(input("Note 1:  "))
    grade2 = float(input("Note 2:  "))
    avarage = (grade1 + grade2) / 2

    student.append(name)
    grades.append(grade1)
    grades.append(grade2)
    student.append(grades[:])
    student.append(avarage)
    all_students.append(student[:])
    student.clear()
    grades.clear()

print("N° NAME       AVARAGE")
for i, j in enumerate(all_students):
    aux = len(all_students[i][0])
    aux = 10 - aux
    print(f"{i} {all_students[i][0]}", " "*aux, f"{all_students[i][2]:>1}")

while True:
    info_student = int(input("Which student do you wanna see grades? Type the number or 999 to leave "))
    if info_student == 999:
        break
    else:
        print(f"Grades of {all_students[info_student][0]}: {all_students[info_student][1]}")

print("Finished program")

#print(all_students)