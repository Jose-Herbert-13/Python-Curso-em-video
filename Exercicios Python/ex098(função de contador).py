from time import sleep


def contador(i, f, p):
    cont = i
    if p<0:
        p *= -1
    if p==0:
        p = 1
    print('-='*35)
    print(f' Contagem de {i} até {f} de {p} em {p}')
    sleep(2)
    if f>i:
        while cont<=f:
            print(f' {cont}', end='', flush=True)
            sleep(0.5)
            cont+=p
    else:
        while cont>=f:
            print(f' {cont}', end='', flush=True)
            sleep(0.5)
            cont-=p
    print(' FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*35)
print(' Agora é sua vez de personalizar o contador: ')
contador(int(input(' Ínicio: ')), int(input(' Fim: ')), int(input(' Passo: ')))
