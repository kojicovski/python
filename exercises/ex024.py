city = input('Type the name of your City').strip()
city = city.upper()


if city.count('SANTO', 0, 5):
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')