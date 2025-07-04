print('    Gerador de PA    ')
print('-='*13)
t = int(input(' Primeiro termo: '))
r = int(input(' Razão: '))
c = 1
while c < 11:
    print(' {} '.format(t), end='→')
    t += r
    c += 1
print(' Fim')