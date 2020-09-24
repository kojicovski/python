num = input('Type a number from 0 to 9999: ')
num1 = int(input('Type another number from 0 to 9999'))

if len(num) == 4:
    print(f'Unit: {num[3]}')
    print(f'Ten: {num[2]}')
    print(f'Hundred: {num[1]}')
    print(f'Thousands: {num[0]}')
elif len(num) == 3:
    print(f'Unit: {num[2]}')
    print(f'Ten: {num[1]}')
    print(f'Hundred {num[0]}')
    print(f'Thousands: 0')
elif len(num) == 2:
    print(f'Unit: {num[1]}')
    print(f'Ten: {num[0]}')
    print(f'Hundred: 0')
    print(f'Thousands: 0')
elif len(num) == 1:
    print(f'Unit: {num}')
    print(f'Ten: 0')
    print(f'Hundred: 0')
    print(f'Thousands: 0')

#Doing with math

u = (num1 // 1 % 10)
d = (num1 // 10 % 10)
c = (num1 // 100 % 10)
m = (num1 // 1000 % 10)

print(f'Unit: {u}')
print(f'Ten: {d}')
print(f'Hundred: {c}')
print(f'Thousands: {m}')