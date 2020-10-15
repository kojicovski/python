num1 = int(input('Type a value: '))
num2 = int(input('Type a value: '))
num3 = int(input('Type a value: '))
num4 = int(input('Type a value: '))

tup = (num1, num2, num3, num4)

count9 = 0
index = 0

for i in range(4):
    if tup[i] == 9:
        count9+=1

print('The number 9 appear {} times'.format(count9))
print('First 3 in position: {}'.format(tup.index(3)))
print(tup)