from random import randint
import time

games = int(input("How many games u wanna do? "))

mega = []
aux = []


for i in range(0, games):
    j = 0
    mega.append(aux[:])
    while j != 6:
        num = randint(1, 60)
        if num not in mega[i]:
                mega[i].append(num)
                j += 1

for i in range(games):
    print(f"Bet {i}: {mega[i]}")
    time.sleep(0.3)