li = list()

while True:
    num = int(input("Type a number: "))
    if num == 999:
        break

    li.append(num)

print(f"{len(li)} number was typed")
li.sort(reverse=True)
print(li)

if 5 not in li:
    print("Number 5 dont was typed")
else:
    print("Number 5 is in the list")