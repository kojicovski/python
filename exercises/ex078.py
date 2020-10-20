num = list()
maxi = list()
mini = list()

for j, i in enumerate(range(0, 5)):
    num.append(int(input(f"Type {j}° number: ")))

for j in range(0, 5):
    maxi_get = max(num)
    mini_get = min(num)

    if num[j] == maxi_get:
        maxi.append(j)
    if num[j] == mini_get:
        mini.append(j)

print(f"You type {num}")
print(f"The bigger value is: {max(num)} in the position ", end="")
for i in maxi:
    print(i, end="...")
print(f"\nThe Smaller value is: {min(num)} in the position ", end="")
for i in mini:
    print(i, end="...")