year = int(input('Type the year'))

print(year/4)

if year % 400 == 0:
    print('Bissexto')
elif year % 4 == 0:
    print('Bisexto')
else:
    print('not bisexto')