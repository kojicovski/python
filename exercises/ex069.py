age = 0
sex = ''
count_age = 0
count_men = 0
count_woman = 0

while True:
    age = int(input('Type an age: '))
    sex = str(input('Type the sex [F/M]: '))

    while sex not in 'FfMm':
        sex = str(input('Type the sex [F/M]: '))

    cont = str(input('Do you wanna continue? [Y/N]: '))

    if sex in 'Ff' and age < 20:
        count_woman += 1
    elif sex in 'Mm':
        count_men +=1

    if age > 18:
        count_age +=1

    while cont not in 'YyNn':
        cont = str(input('Do you wanna continue? [Y/N]: '))

    if cont in 'Nn':
        break

print('-'*20)
print(f'{count_age} people are under 18 years old')
print('-'*20)
print(f'{count_men} men registered')
print('-'*20)
print(f'{count_woman} woman are under 20 years old')