lista = list()
impar = list()
par = list()
while True:
    lista.append(int(input(' Digite um valor: ')))
    r = str(input(' Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input(' Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
for v in lista:
    if v%2==0:
        par.append(v)
    else:
        impar.append(v)
print('-='*35)
print(f' A lista completa é {lista}')
print(f' A lista de Pares é {par}')
print(f' A lista de Impares é {impar}')
