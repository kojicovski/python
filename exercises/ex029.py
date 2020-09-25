vel = float(input('Velocity of yhe car: '))
traf_ticket = 0

if vel > 80:
    print('Your received a traffic ticket, your velocity was {:.1f}km/h'.format(vel))
    traf_ticket = (vel - 80) * 7
    print('You need to pay R${:.2f}'.format(traf_ticket))
else:
    print('Its OK!')