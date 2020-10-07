num = int(input('Type a number and see your multiplication table: '))

while True:
    if num < 0:
        break
    for i in range(11):
        mult = num * i
        print(f'{num} x {i} = {mult}')
    num = int(input('Type a number and see your multiplication table: '))
print("Programm finished!")