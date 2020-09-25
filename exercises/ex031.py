trip = float(input('How far is your trip?'))
ticket = 0

if trip <= 200:
    ticket = trip * 0.50
    print('Your trip have {}km. Bus ticket R${}!'.format(trip, ticket))
else:
    ticket = trip * 0.45
    print('Your trip have {}km. Bus ticket R${}!'.format(trip, ticket))