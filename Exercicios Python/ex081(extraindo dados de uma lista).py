lista = list()
while True:
    lista.append(int(input(' Digite um valor: ')))
    r = str(input(' Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'NS':
        r = str(input(' Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-='*30)
print(f' Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f' Os valores em ordem decrecente são: {lista}')
if 5 in lista:
    print(' O valor 5 faz parte da lista! E se encontra nas posições: ', end='')
else:
    print(' O valor 5 não faz parte da lista!')
