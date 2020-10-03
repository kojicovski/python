sex = ''

while sex != 'M' or sex  != 'F':
    sex = str(input("Type your sex: "))
    if sex == 'M' or sex == 'F':
        print('Ok')
        break