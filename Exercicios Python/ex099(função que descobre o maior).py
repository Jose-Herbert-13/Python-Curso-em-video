from time import sleep


def maior(*n):
    cont = maior = 0
    print('-='*35)
    print(' Analisando os valores passados...')
    for v in n:
        print(f' {v}', end='', flush=True)
        sleep(0.3)
        if cont==0 or v>maior:
            maior = v
        cont += 1
    sleep(0.5)
    print(f'\n Ao todo foram informados {cont} valores')
    print(f' E o maior valor foi {maior}')
    sleep(1)


maior(2, 9, 4, 13, 7, 5, 8, 0, 1, 6)
maior(32, 4, 17, 5, 8, 90, 1, 6)
maior(82, 4, 7, 25, 0, 1)
maior(92, 24, 5, 100)
maior()
