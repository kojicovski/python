num = int(input('Type a number between 1 to 9: '))
mult_table = 0

for i in range(0,10):
    mult_table = num * i
    print('{} x {} = {}'.format(num,i,mult_table))