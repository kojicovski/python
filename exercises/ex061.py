first_term = int(input('Type first term of an arithmetic progression: '))
ratio = int(input('Type the ratio: '))

fr = 0
i = 0
quant = 11

while i != quant and quant != 0:
    fr = first_term + (i - 1) * ratio
    i+=1
    print(fr)

    if i == quant:
        i = 0
        quant = int(input('Do u wanna continue? Enter how many terms u wanna see: '))