import random

num = []
li_even = []
li_odd = []

for i in range(7):
    #add_num = int(input("Type a number"))
    add_num = random.randint(1, 10)

    if add_num % 2 == 0:
        li_even.append(add_num)
    else:
        li_odd.append(add_num)

num.append(li_even[:])
num.append(li_odd[:])
print(f"Full list: {num}")
print(f"Even numbers: {num[0]}")
print(f"Odd numbers: {num[1]}")
