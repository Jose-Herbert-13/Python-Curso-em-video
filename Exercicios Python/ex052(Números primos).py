n = int(input(' Digite um número: '))
d = 0
for c in range(1, n+1):
    if n%c == 0:
        print('\033[32m', c, '\033[m', end='')
        d += 1
    else:
        print('\033[31m', c, '\033[m', end='')
print('\n O número {} foi divisível() {} vezes'.format(n, d))
if d<=2:
    print(' Então ele é primo')
else:
    print(' Então ele não é primo')