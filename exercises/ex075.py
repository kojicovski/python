num1 = int(input('Type a value: '))
num2 = int(input('Type a value: '))
num3 = int(input('Type a value: '))
num4 = int(input('Type a value: '))

tup = (num1, num2, num3, num4)

count9 = 0

for i in range(4):
    if tup[i] == 9:
        count9+=1

print('The number 9 appear {} times'.format(count9))

if 3 not in tup:
    print('Dont have 3 in the tuple')
else:
    print('First 3 in position: {}'.format(tup.index(3)))

print('The Even numbers is: ', end='')

for i in range(4):
    if tup[i] % 2 == 0:
        print(tup[i], end=' ')

print('\n{}'.format(tup))