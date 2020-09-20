from random import sample

alunos = 'Samuel', 'Joao', 'Maria', 'Gabi'
sort = sample(alunos,4)

for i in range(4):
    print(sort[i])