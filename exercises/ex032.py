from datetime import date

year = int(input('Type the year: '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is a leap year')
else:
    print("This isn't a leap year")