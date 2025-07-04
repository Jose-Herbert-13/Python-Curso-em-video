from time import sleep


def fatorial(n, show):
    """
    --> Calcula o fatorial de um número, sendo:
        n = número
        show = se vai ou não mostrar o calculo
        return = Resultado
    """
    f = 1
    print('-'*70)
    print(f' Calculando fatorial de {n}:')
    print('-'*70)
    for c in range(n, 0, -1):
        f *= c
        if show==True:
            print(f' {c} ', end='', flush=True)
            print('x' if c>1 else '= ', end='')
            sleep(0.3)
    return f


num = int(input(' Digite um número para ver o seu fatorial: '))
l = str(input(' Quer ver o calculo? [S/N] ')).upper().strip()[0]
while l not in 'NS':
    l = str(input(' Quer ver o Calculo? [S/N] ')).upper().strip()[0]
t = True if l=='S' else False
print(fatorial(num, t))

