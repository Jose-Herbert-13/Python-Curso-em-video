from random import randint
from time import sleep
it = ('Pedra', 'Papel', 'Tesoura')
nc = randint(0,2)
print(''' \033[7mOpções:\033[m
 \033[2;31m[0] Pedra\033[m
 \033[2;31m[1] Papel\033[m
 \033[2;31m[2] Tesoura\033[m''')
np = int(input(' Qual é a sua jogada?'))
print(' JO')
sleep(1)
print(' KEN')
sleep(1)
print(' PÔ!!!')
print('-='*13)
print(' Computador jogou: {}'.format(it[nc]))
print(' Jogador jogou: {}'.format(it[np]))
print('-='*13)
if nc == 0:
    if np == 0:
        print(' EMPATE')
    elif np == 1:
        print(' JOGADOR VENCE')
    else:
        print(' SISTEMA VENCE')
elif nc == 1:
    if np == 0:
        print(' SISTEMA VENCE')
    elif np  == 1:
        print(' EMPATE')
    else:
        print(' JOGADOR VENCE')
else:
    if np == 0:
        print(' JOGADOR VENCE')
    elif np == 1:
        print(' SISTEMA VENCE')
    else:
        print(' EMPATE')
