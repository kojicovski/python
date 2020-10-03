num1 = int(input('Type first number: '))
num2 = int(input('Type second number: '))

print('What u want to do?')

menu = int(input('1 - To sum \n2 - To multiplication\n3 - Higher number\n4 - News numbers\n5 - Exit\n'))

class Calc():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum1(self):
        sum1 = self.num1 + self.num2
        return sum1

    def mult(self):
        mult = self.num1 * self.num2
        return mult
    
    def heigher(self):
        if self.num1 > self.num2:
            heigher = self.num1
        else:
            heigher = self.num2
        return heigher

calc = Calc(num1, num2)

while menu != 5:
    if menu == 1:
        print(f'Sum of {num1} + {num2} = {calc.sum1()}')
        menu = 6
    if menu == 2:
        print(f'Mult of {num1} + {num2} = {calc.mult()}')
        menu = 6
    if menu == 3:
        print(f'Higher Number is {calc.heigher()}')
        menu = 6
    if menu == 4:
        num1 = int(input('Type first number: '))
        num2 = int(input('Type second number: '))
        calc = Calc(num1, num2)
        menu = 6
    if menu == 6:
        print('Chose again:')
        menu = int(input('1 - To sum \n2 - To multiplication\n3 - Higher number\n4 - News numbers\n5 - Exit \n'))

print('Thanks to used the programm')