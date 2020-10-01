class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def foo(self):
        #return f'Your weight is {self.weight}Kg, to have {self.age} and you are {self.sex}'
        return self.name, self.age, self.sex


p = []

for i in range(2):
    name = str(input(f'{i}-Whats your name: '))
    age = int(input(f'{i}-Type your age: '))
    sex = str(input(f'{i}-Type your sex: ')).strip()
    p.append(People(name, age, sex))
    print(p[i].foo())

aveg_age = 0.0
old_guy = ''
age_old_guy = 0
male_count = 0

for i in range(2):
    aveg_age = (aveg_age + p[i].age)
    if i > 0:
        aveg_age = aveg_age / (i+1)
    if p[i].sex == 'male' and p[i].age > age_old_guy:
        age_old_guy = p[i].age
        old_guy = p[i].name
    if p[i].sex == 'female' and p[i].age < 20:
        male_count += 1

print(f'Average age {aveg_age}')
print(f'Old guy is {old_guy}')
print(f'{male_count} women are under 20 years old.')