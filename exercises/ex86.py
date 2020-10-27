import random

mat = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        #num = random.randint(1, 9)
        num = int(input(f"Position {i},{j}: "))
        mat[i].append(num)

for i in range(3):
    print(mat[i])
