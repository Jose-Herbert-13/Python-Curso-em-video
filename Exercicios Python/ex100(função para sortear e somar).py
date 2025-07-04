from random import randint
from time import sleep


def sorteia(lista):
    print(' Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        n = randint(1, 10) 
        print(n, end=' ', flush=True)
        lista.append(n)
        sleep(0.5)
    print('Pronto!')


def somapar(lista):
    s=0
    for v in lista:
        if v%2==0:
            s += v
    print(f' Somando os valores pares de {lista}, temos {s}')


número = list()
sorteia(número)
somapar(número)
