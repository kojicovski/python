from random import randint

num = int(input("Type a number: "))
choice = str(input('Choose even or odd: ')).strip()
num_pc = randint(0,10)
count = 0

while True:
    sum = num + num_pc
    print(f'Sum:{sum}')

    if sum % 2 == 0 and choice == 'E':
        print("Even, you're right")
        count += 1
    elif choice == 'O':
        print("Odd, you're right")
        count += 1
    else:
        print(f'You type {num} and PC {num_pc}')
        print(f"You lose! {count} answers right!")
        break
    num = int(input("Type a number: "))
    choice = str(input('Choose even or odd: ')).split()
    num_pc = randint(0, 10)
