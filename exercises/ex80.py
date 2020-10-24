# num = []
# num_aux = []
#
# for i in range(5):
#     num_add = int(input("Type a number: "))
#     num_aux.append(num_add)
#
# for i in range(5):
#     mini = min(num_aux)
#     num.append(mini)
#     num_aux.remove(mini)
#
# print(num_aux)
# print(num)

li = []

for i in range(5):
    add_num = int(input("Type a number: "))

    if i == 0 or add_num > li[-1]:
        li.append(add_num)
    else:
        for j, k in enumerate(li):
            if add_num <= k:
                li.insert(j, add_num)
                break
print(li)




