import random

mat = [[], [], []]
count_num_odd = 0
third_sum = 0

for i in range(0, 3):
    for j in range(0, 3):
        num = random.randint(1, 9)
        #num = int(input(f"Position {i},{j}: "))
        mat[i].append(num)

for i in range(0, 3):
    for j in range(0, 3):
        if mat[i][j] % 2 == 0:
            count_num_odd += mat[i][j]
    third_sum += mat[i][2]
    print(mat[i])

print(f"sum of odd value: {count_num_odd}")
print(f"Sum of third column: {third_sum} ")
print(f"The bigger value of second line: {max(mat[1])}")
