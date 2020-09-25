import random

num = random.randrange(5)

num1 = int(input('Type a number what u think your computer chose: '))

if num == num1:
    print('You are right!')
else:
    print('You are wrong!')

print(num)
