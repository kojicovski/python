txt = input('Type something')

if txt.isnumeric():
    print(f'{txt} contains only numbers')
elif txt.isalpha():
    print(f'{txt}  contains only chars')
elif txt.isalnum():
    print(f'{txt} contains numbers and chars')
