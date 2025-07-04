from time import sleep
n1 = int(input(' Primeiro valor: '))
n2 = int(input(' Segundo valor: '))
r = 0
while r != 5:
    print('''    [ 1 ] Soma
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa ''')
    r = int(input('>>>> Qual sua opção? '))
    if r == 1:
        soma = n1 + n2
        print(' O resultado é {} + {} = {}'.format(n1, n2, soma))
    elif r == 2:
        produto = n1*n2
        print(' O resultado é {} × {} = {}'.format(n1, n2, produto))
    elif r == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(' O maior valor entre {} e {} é {}'.format(n1, n2, maior))
    elif r == 4:
        print(' Informe os números novamente:')
        n1 = int(input(' Primeiro valor: '))
        n2 = int(input(' Segundo valor: '))
    elif r == 5:
        print(' Finalizando...')
    else:
        print(' Opção inválida, tente novamente')
    print('-=-'*15)
    sleep(1)
print(' Fim do programa! Volte sempre!')