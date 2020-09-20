#import --> import everything of module
#from food import pudim --> import just what u wanna use

from math import sqrt
import random

num = int(input('Type a number: '))
root = sqrt(num)

num2 = random.randint(1,50)

print(f'Square root of {num} is {root:.2}')
print('Test random() func : {}'.format(num2))

