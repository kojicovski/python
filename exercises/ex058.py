import random

num = random.randrange(10)
right_num = 11
count = 0

while num != right_num:
    right_num = int(input('Type a number: '))
    if right_num == num:
        print('You are right after {} answer'.format(count))
        break
    else:
        print("Try again, you missed!")
        count+=1