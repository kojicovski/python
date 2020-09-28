first_term = int(input('Type first term of an arithmetic progression '))
ratio = int(input('Type the ratio'))

fr = 0

for i in range(1,11):
    fr = first_term + (i - 1) * ratio
    print(fr)