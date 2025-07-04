from random import randint
from time import sleep
n = randint(0, 5) #número aleatorio
print('\033[1;35m')
print('-=-'*17)
print(' Vou pensar em um número de 0 a 5, tente advinhar')
print('-=-'*17)
print('\033[4;37m')
j = int(input(' Em que número eu pensei? ')) #jogador
print(' PROCESSANDO...')
sleep(2)
if n==j:
    print(' Você ganhou, meu número foi {}'.format(n))
else:
    print(' Você errou, meu número foi {}'.format(n))
print('\033[m')
    