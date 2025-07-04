n = int(input(' Digite um valor: '))
print(' A tabuada desse valor é:')
for c in range(1, 11):
    print(' {} x {:2} = {}'.format(n, c, n*c))