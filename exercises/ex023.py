from math import trunc

num = input('Type a number from 0 to 9999: ')
num1 = int(input('Type another number from 0 to 9999'))

if len(num) == 4:
    print(f'Unidade: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')
elif len(num) == 3:
    print(f'Unidade: {num[2]}')
    print(f'Dezena: {num[1]}')
    print(f'Centena {num[0]}')
    print(f'Milhar: 0')
elif len(num) == 2:
    print(f'Unidade: {num[1]}')
    print(f'Dezena: {num[0]}')
    print(f'Centena: 0')
    print(f'Milhar: 0')
elif len(num) == 1:
    print(f'Unidade: {num}')
    print(f'Dezena: 0')
    print(f'Centena: 0')
    print(f'Milhar: 0')

if num1 > 999:
    aux1 = num1 / 1000
    print(f'Milhar{trunc(aux1)}')

    aux2 = num1 / 100
    aux2 = aux2 // 10
    print(f'Dezena')

#Need a feature