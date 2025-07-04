print('='*30)
print('    10 TERMOS DE UMA PA    ')
print('='*30)
pt = int(input(' Primeiro termo: '))
r = int(input(' Razão: '))
d = pt + (10 - 1) * r
for c in range(pt, d+1, r):
    print(' {} '.format(c), end='→')
print(' ACABOU')