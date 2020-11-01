student = {}

student["Name"] = str(input("Name: "))
student["Avarage"] = float(input("Avarage: "))

if student["Avarage"] >= 7:
    student["Status"] = "Approved"
else:
    student["Status"] = "Not approved"

for k, v in student.items():
    print(f"{k}: {v}")