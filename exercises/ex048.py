sum = 0

for i in range(3,501,3):
    if i % 2 != 0:
        sum = sum + i
        print(i)
print('Sum = {}'.format(sum))