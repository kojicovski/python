words = 'rice', 'learning', 'samuel', 'kkk'

for i in range(len(words)):
    print(f'\nThe word {words[i]} have:', end='')
    if words[i].find("a") != -1:
        print('a', end='-')
    if words[i].find("e") != -1:
        print('e', end='-')
    if words[i].find("i") != -1:
        print('i', end='-')
    if words[i].find("o") != -1:
        print('o', end='-')
    if words[i].find("u") != -1:
        print('u', end='-')