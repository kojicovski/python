class Product():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def foo(self):
        return self.name, self.value


total = 0
cheaper_name = ''
cheaper_value = 0
over_thous = 0
prod = []
i = 0

print("="*10,"Welcome to Samu'Store","="*10)

while True:
    cad_prod = str(input('Type the name of the product: '))
    value_prod = float(input('Type the value: $'))
    prod.append(Product(cad_prod, value_prod))

    cont = str(input('Do you wanna continue? [Y/N] '))

    total = prod[i].value + total

    if prod[i].value > 1000:
        over_thous += 1

    if prod[i].value <= prod[i-1].value:
        cheaper_name = prod[i].name
        cheaper_value = prod[i].value

    i += 1

    while cont not in 'YyNn':
        cont = str(input('Do you wanna continue? [Y/N] '))

    if cont in 'Nn':
            break

print('+'*25)
print(f'Total purchases: ${total}')
print(f'We have {over_thous} that costs more than $1000')
print(f'The cheaper product is {cheaper_name} and costs ${cheaper_value}')