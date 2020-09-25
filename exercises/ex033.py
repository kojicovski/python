num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
num3 = int(input('Number 3: '))

if num1 > num2 and num1 > num3:
    print('Bigger {}'.format(num1))
    if num2 > num3:
        print('Medium {}'.format(num2))
        print('Smaller {}'.format(num3))
    else:
        print('Medium {}'.format(num3))
        print('Smaller {}'.format(num2))
elif num2 > num1 and num2 > num3:
    print('Bigger {}'.format(num2))
    if num1 > num3:
        print('Medium {}'.format(num1))
        print('Smaller {}'.format(num3))
    else:
        print('Medium {}'.format(num3))
        print('Smaller {}'.format(num1))
elif num3 > num2 and num3 > num1:
    print('Bigger {}'.format(num3))
    if num1 > num2:
        print('Medium {}'.format(num1))
        print('Smaller {}'.format(num2))
    else:
        print('Medium {}'.format(num2))
        print('Smaller {}'.format(num1))