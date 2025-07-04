from random import randint
from time import sleep
mega = []
jogo = []
print('-'*40)
print(f"{'JOGA NA MEGA SENA':^40}")
print('-'*40)
q = int(input(' Quantos jogos você quer que eu sorteie? '))
for c in range(0, q):
    for j in range(0, 6):
        n = randint(1, 60)
        while n in jogo:
            n = randint(1, 60)
        jogo.append(n)
    jogo.sort()
    mega.append(jogo[:])
    jogo.clear()
print( )
print(f"-=-=-=-=-=-= SORTEANDO {q} JOGOS =-=-=-=-=-=-")
for c, v in enumerate(mega):
    sleep(1)
    print(f' Jogo {c+1}: {v}')
print('-=-=-=-=-=-= >BOA SORTE!< =-=-=-=-=-=-')
