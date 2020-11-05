people_list = []
people_dict = {}
count = 0
avarage_age = 0
while True:
    name = str(input("Name: "))
    if name == "exit":
        break
    sex = str(input("Sex [M/F]:"))
    age = int(input("Age:"))

    avarage_age = (age + avarage_age)

    people = {"name": name, "sex": sex, "age": age}
    people_dict[f"people{count}"] = people
    count += 1

avarage_age = avarage_age / count

people_list.append(people_dict)
print(f"- Registered people {count}")
print(f"- Avarage age: {avarage_age}")
for i in people_list:
    print(f"- Woman registered: ", end="")
    for j in i.values():
        if j["sex"] in "Ff":
            print(f"{j['name']}", end=",")
print()
for i in people_list:
    print(f"- Age more than avarage age:")
    for j in i.values():
        if j["age"] > avarage_age:
            for k, v in j.items():
                print(f"{k} = {v}", end="; ")
            print()
