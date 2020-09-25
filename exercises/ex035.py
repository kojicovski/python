a = int(input('Value a: '))
b = int(input('Value b: '))
c = int(input('Value c: '))

if a > b-c and a < b+c and b > a-c and b < a+c and c > a-b and c < a+b:
    print('You can do a triangle')
else:
    print('You cant do a triangle')