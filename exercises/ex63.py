num = int(input('Type a number and see sequence of fibonnaci: '))
c = 0

fib = [0,1]

while fib[c] < num:
    fib.append(fib[c+1] + fib[c])
    c+=1
    print(fib[c])