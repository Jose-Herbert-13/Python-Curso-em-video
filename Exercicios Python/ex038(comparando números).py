a = int(input(' \033[32mDigite um número inteiro:\033[m '))
b = int(input(' \033[31mDigite outro número:\033[m '))
if a>b:
    print(' O \033[2;32mPrimeiro\033[m valor é Maior!')
elif b>a:
    print(' O \033[2;31mSegundo\033[m valor é Maior!')
else:
    print(' \033[33mNão existe valor Maior, os dois são Iguais!\033[m')