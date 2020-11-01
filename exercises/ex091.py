from random import randint

players = {}

for i in range(4):
    players[f"Player{i+1}"] = randint(1, 6)

print("Values drawn: ")
for k, v in players.items():
    print(f"{k}: {v}")

print("Ranking: ")
rank = 1
copy = []
for i in sorted(players.values(), reverse=True):
    for k, v in players.items():
        if v == i:
            if k not in copy:
                print(f"{rank}° place: {k} with {i} points")
                copy.append(k)

                rank += 1
                break
