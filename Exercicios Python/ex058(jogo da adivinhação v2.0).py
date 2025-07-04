from random import randint
from time import sleep
n = randint(0, 10) #número aleatorio
j = 11
t = 0
acertou = False
print('\033[1;35m')
print('-=-'*17)
print(' Vou pensar em um número de 0 a 10, tente advinhar')
print('-=-'*17)
while not acertou:
    print('\033[4;37m')
    j = int(input(' Em que número eu pensei?\033[m ')) #jogador
    print(' PROCESSANDO...')
    sleep(1)
    t += 1
    if j == n:
        acertou = True
    else:
        if j < n:
            print(' Mais..., tente de novo')
        elif j > n:
            print(' Menos..., tente de novo')
print(' \033[32mVocê acertou, Parabéns. \n Você precisou de {} tentativas para acertar. \033[m'.format(t))
