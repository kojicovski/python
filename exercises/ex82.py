li= []
li_even = []
li_odd = []

while True:
    add_num = int(input("Type a number: "))

    if add_num == 999:
        break
    li.append(add_num)

    if add_num % 2 == 0:
        li_even.append(add_num)
    else:
        li_odd.append(add_num)

li.sort()
li_odd.sort()
li_even.sort()

print(f"Full list{li}")
print(f"Even list {li_even}")
print(f"Odd list {li_odd}")