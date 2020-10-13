tup = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')

num = int(input('Type a number: '))

while True:
    for i in tup:
        count = tup.index(i)
        if num == count:
            print(i)
            num = int(input('Type a number: '))
    if num == 999:
        print('The end')
        break