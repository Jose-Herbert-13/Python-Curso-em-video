lista = list()
while True:
    n = int(input(' Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print(' Valor adicionado com sucesso...')
    else:
        print(' Valor duplicado! Não vou adicionar...')
    r = str(input(' Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'NS':
        r = str(input(' Tente novamente. Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break
lista.sort()
print('-='*25)
print(f' Você digitou os valores: {lista}')
