tup = ('Bread', 1.4, 'Cheese', 3.5, 'Pork', 20.00, 'Beef', 100.00, 'Motorcycle', 1000.00)

print('='*17, 'Value list', '='*17)

for i in range(0, len(tup)-1,2):
    point = 37 - len(tup[i])
    print(f'* {tup[i]}', '.'*point, f'$ {tup[i+1]:>6} *')

print('='*46)