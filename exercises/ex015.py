kmRun = float(input('Km drived: '))
daysUsed = int(input('Days used: '))

pay = (daysUsed * 60) + (kmRun * 0.15)

print(f'Your bill is R${pay}')
