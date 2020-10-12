print("="*30)
print('BANCO SAMUKOVSKI')
print("="*30)

withdraw = int(input('Type the value that you wanna withdraw money: $'))

print(withdraw)

while True:

    if withdraw > 0:
        take_f = (withdraw // 50)
        withdraw = withdraw - (take_f * 50)
        take_t = (withdraw // 20)
        withdraw = withdraw - (take_t * 20)
        take_ten = (withdraw // 10)
        withdraw = withdraw - (take_ten * 10)
        take_one = withdraw
        break
    else:
        print(f'Impossible withdraw R${withdraw}')
        break


print(f"{take_f} notes of $50")
print(f"{take_t} notes of $20")
print(f"{take_ten} notes of $10")
print(f"{take_one} notes of $1")