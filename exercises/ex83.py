ex = str(input("Type a expression: "))
li = []
count1 = 0
count2 = 0

for i, j in enumerate(ex):
    li.append(j)

    if "(" in li[i]:
        count1 += 1
    elif ")" in li[i]:
        count2 += 1

if count1 != count2:
    print("Wrong expression")
else:
    print("Expression OK")