import datetime

people = {}
x = datetime.datetime.now()
x = int(x.strftime("%Y"))

people["Name"]= str(input("Name: "))
age = int(input("Year of Birth: "))
age = x  - age
people["Age"] = age
people["WorkCard"] = int(input("Work Card: "))

if people["WorkCard"] == 0:
    for v, k in people.items():
        print(f"{k}: {v}")
else:
    people["Hiring"] = int(input("Year of Hiring: "))
    people["Salary"] = float(input("Salary: R$"))
    people["Retirement"] = 35 - (x - people["Hiring"]) + people["Age"]
    for v, k in people.items():
        print(f"{v}: {k}")