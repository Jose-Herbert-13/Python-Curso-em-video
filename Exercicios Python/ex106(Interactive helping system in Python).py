c = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;30m')    #0 sem cor, 1 vermelho, 2 verde, 3 amarelo, 4 azul, 5 roxo, 6 branco


def ajuda(hl):
    txt(f'Acessando manual do comando\'{hl}\'', 4)
    print(f'{c[6]}', help(hl), f'{c[0]}')


def txt(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)
    print(c[0])


while True:
    txt('  SISTEMA DE AJUDA PYHELP  ', 3)
    f = str(input(' Função ou Biblioteca > '))
    if f.upper()=='FIM':
        break
    ajuda(f)
txt('  ATÉ LOGO  ', 1)
