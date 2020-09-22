name = 'Samuel Kojicovski Gabriela Dias De Oliveira'

print(name.upper())
print(name.lower())

union = name.split()


def count(my_str):
    glob = 0
    for lista in my_str:
        glob = glob + len(lista)
    return glob

print(count(union))
print(len(union[0]))