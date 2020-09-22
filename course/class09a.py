

frase = 'Curso em Vídeo Python, testando tratamento de strings'
print(frase[::2])
print(len(frase))
print(frase.count('a'))
print('Python' in frase)
print(frase.find('testando'))

lista = frase.split()

print('Lista de frase : {}'.format(lista))


arquivo = open('python-test.txt', 'r')

for list in arquivo:
    valores = list.split()
    print(valores)