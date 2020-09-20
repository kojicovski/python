from math import hypot

adj = int(input('Type adjacent side of triangle'))
op = int(input('Type opposite side of triangle'))

print('Value of hypotenuse is {}'.format(hypot(adj,op)))
