num = 0
sum = 0

print('Type 6 whole numbers: ')
for i in range(1,6+1):
    num = int(input())
    if  num % 2 == 0:
        sum = sum + num
print('Sum = {}'.format(sum))