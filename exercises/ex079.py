num = list()
i = 0

while True:
    num_add = int(input("Type a number: "))
    if num_add == 99:
        break
    elif num_add not in num:
        num.append(num_add)


print(sorted(num))
