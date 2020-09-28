from time import sleep

start = int(input('Type 1 to start the fireworks: '))
print('Starting...')
for i in range(1,10+1):
    sleep(1)
    print(f'{i}s')
sleep(1)
print('Happy new year!!')