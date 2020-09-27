num = int(input('Type a number: '))
menu = int(input('Type:\n 1 to convert to HEX!\n 2 to convert to OCT!\n 3 to convert to BIN!Type here: \n'))

if menu == 1:
    print(hex(num).upper())
elif menu == 2:
    print(oct(num).upper())
elif menu == 3:
    print(bin(num).upper())