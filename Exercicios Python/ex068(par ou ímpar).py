from random import randint
s = v = 0
r = ''
print('\033[36m')
print('-='*30)
print('        Vamos Jogar Par ou Ímpar')
print('-='*30)
print('\033[m')
while True:
    vj = int(input(' Diga um valor: '))
    vc = randint(0,10)
    s = vc + vj
    pi = str(input(' Par ou Ímpar? [P/I] ')).strip().upper()[0] 
    while pi not in 'PI':
        pi = str(input(' Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*60)
    print(f' Você jogou {vj} e o Computador {vc}. Total de {s}', end='')
    print(' Deu PAR' if s%2==0 else ' Deu ÍMPAR')
    print('-'*60)
    if pi == 'P':
        if s%2==0:
            print('\033[32m Você VENCEU \033[m')
            print(' Vamos Jogar Novamente...')
            v += 1
        else:
            print('\033[31m Você PERDEU \033[m')
            break
    else:
        if s%2==0:
            print('\033[31m Você PERDEU \033[m')
            break
        else:
            print('\033[32m Você VENCEU \033[m')
            print(' Vamos jogar novamente...')
            v += 1
if v < 2:
    print('\033[31m')
elif v < 5:
    print('\033[33m')
else:
    print('\033[32m')
print('-='*30)
print(f' GAME OVER. Você venceu um total de {v} vezes \033[m')
