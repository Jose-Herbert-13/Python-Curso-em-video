print('    Gerador de PA    ')
print('-='*13)
t = int(input(' Primeiro termo: '))
r = int(input(' Razão: '))
c = 1
mais = 10
total = 0
q = 0
while mais != 0:
    total += mais
    while c <= total:
        print(' {} '.format(t), end='→')
        t += r
        c += 1
        q += 1
    print(' PAUSA')
    mais = int(input(' Quantos termos você quer mostrar q mais? '))
print(' Progressão Finalizada com {} termos mostrados'.format(q))