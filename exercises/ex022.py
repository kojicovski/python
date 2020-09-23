name = 'Samuel Kojicovski Gabriela Dias De Oliveira'

print(name.upper())
print(name.lower())


#Another way to count the letter without space
print('Your name have {} letters'.format(len(name) - name.count(' ')))

union = name.split()


def count(my_str):
    glob = 0
    for lista in my_str:
        glob = glob + len(lista)
    return glob

print(count(union))
print(len(union[0]))