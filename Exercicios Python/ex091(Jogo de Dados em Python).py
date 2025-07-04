from random import randint
from time import sleep
from operator import itemgetter
jogo  = {'Jogador 1': randint(1,6),  
                       'Jogador 2': randint(1,6), 
                       'Jogador 3': randint(1,6), 
                       'Jogador 4': randint(1,6)}
ranking = list()
print('-='*35)
print(' Valores sorteados')
for k, v in jogo.items():
    print(f' O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*35)
for c, v in enumerate(ranking):
    print(f' {c+1}° lugar: {v[0]} com {v[1]}')
