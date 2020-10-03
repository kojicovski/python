#factorial

fac = int(input('Type a number and see your factorial: '))

c = 1
num = fac

while c != num:
        fac = fac * c
        c = c + 1
        print(c,fac)
print(fac)

for i in range(1,num):
    num = num * i
print(num)