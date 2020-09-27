price_house = float(input('How much this house? '))
money_buyer = float(input('Type how much money u have: '))
years =  int(input('How many years do u want to pay the house?'))

installment = price_house / years

if installment > (money_buyer * 30/100):
    print("I'm sorry, you can only spend 30% of your salary!")
else:
    print('The house is your, congrats!!!')
