goal = []
total = 0
player = {}
count = 0
while True:
    name = (str(input("Name of player: ")))
    if name == "exit":
        break
    match = int(input(f"How many match {name} played?"))

    for i in range(match):
        inp = int(input(f"How many goals in the match {i}?"))
        goal.append(inp)
        total += inp

    player[f'{count}'] = {"name": name, "goals": goal[:], "total": total}
    goal.clear()
    count += 1
    total = 0

print("="*35)
print("Cód   Name      Goals        total")
print("-"*31)
for i in player.keys():
    print(f"{i}   ", end=" ")
    for v, k in player[f"{i}"].items():
        try:
            width = len(k)
        except TypeError:
            pass
        print(f" {k}", " "*width, end="")
    width = 0
    print()

while True:
    show = str(input("How player do u wanna see status of match?"))
    if show == "exit":
        break

    print(f"======{player[f'{show}']['name']} status ======")
    count1 = 0
    for i in player[f"{show}"]["goals"]:
        print(f"In the game {count1} scored {i} goals")
        count1 += 1


print("Ending the programm")




