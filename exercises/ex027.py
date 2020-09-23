name = input('Type your full name: ')

name_aux = name.split()
last_name = len(name_aux) - 1

print('First name: {}'.format(name_aux[0]))
print('Last name: {}'.format(name_aux[last_name]))