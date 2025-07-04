print('-'*30)
print('  Sequêcia de Fibonacci  ')
print('-'*30)
n = int(input(' Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 1
print('~'*70)
while c <= n:
    print(' {} '.format(t1), end='→')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
print(' Fim')
print('~'*70)
