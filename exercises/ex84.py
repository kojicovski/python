people_info = []
peoples = []
weighter = 0
lighter = 0

while True:
    name = str(input("Type a name or exit to leave: "))
    if name == "exit":
        break
    weight = int(input("Type the weight: " ))

    people_info.append(name)
    people_info.append(weight)
    peoples.append(people_info[:])
    people_info.clear()


print(f"You registered {len(peoples)} peoples")

weighter = lighter = peoples[0][1]

for i in range(len(peoples)):
    if peoples[i][1] > weighter:
        weighter = peoples[i][1]
    elif peoples[i][1] <= lighter:
        lighter = peoples[i][1]
print(f"Weigter is {weighter} Kg. Weight of ",end="")
for i in range(len(peoples)):
    if peoples[i][1] >= weighter:
        print(peoples[i][0], end=" | ")
print()
print(f"Lighter is {lighter} Kg. Weight of ",end="")
for i in range(len(peoples)):
    if peoples[i][1] <= lighter:
        print(peoples[i][0], end=" | ")
print()

