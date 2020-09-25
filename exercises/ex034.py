salary = float(input('Type your salary: '))

if salary < 1250:
    salary = salary + salary * (15/100)
else:
    salary = salary + salary * (10/100)

print('Your new salary: {:.1f}'.format(salary))