from typing import List, Any

player = {"name": str(input("Name of player: "))}

match = int(input(f"How many match {player['name']} played?"))
goal = []
total = 0

for i in range(match):
    inp = int(input(f"How many goals in the match {i}?"))
    total += inp
    goal.append(inp)

player["goal"] = goal
player["total"] = total

for v, k in player.items():
    print(f"The value '{v}' have content '{k}'")

print(f"The player {player['name']} played {match} matches")
count = 0
for i in player["goal"]:
    print(f"In the match {count}: scored {i}")
    count += 1
print(f"There were {player['total']} goals")


