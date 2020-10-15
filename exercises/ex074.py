import random

tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
       random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
       )

bigger = 0
smaller = 255

for i in range(5):
    if tup[i] > bigger:
        bigger = tup[i]
    elif tup[i] < smaller and tup[i] != 0:
        smaller = tup[i]

print(type(tup))
print(tup)

print('bigger {}'.format(bigger))
print('smaller {}'.format(smaller))