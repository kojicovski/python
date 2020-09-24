txt = str(input('Type your text')).lower().strip()

print('Your text have {} letters'.format(txt.count('a')))
print('First appear in position: {}'.format(txt.find('a')))
print('Last appear in position: {}'.format(txt.rfind('a')))
