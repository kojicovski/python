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

    if li == []:
        li.append(li)
        print("Num added to list")
    elif max(li) < add_num:
        li.append(add_num)
        print("Num added at the end of the list")
    elif min(li) > add_num:
        li.insert(add_num, 0)
        print("Num added at the beginning of the list")
    else:
        for j, k in enumerate(li):
            if k > add_num:
                li.insert(j, add_num)
                print(f'Número {add_num} adicionado na posição {j}')
                break
            if k == add_num:
             break



