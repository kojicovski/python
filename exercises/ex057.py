sex = str(input("Type your sex: ")).strip().upper()[0]

while sex not in 'MmFf':
    sex = str(input("Invalid Data. Type your sex: ")).strip().upper()[0]
print('Sex registered successfully')