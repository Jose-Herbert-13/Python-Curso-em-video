pessoas = []
dados = []
ma = me = 0
while True:
    dados.append(str(input(' Nome: ')).strip())
    dados.append(float(input(' Peso: ')))
    if len(pessoas)==0:
        ma = me = dados[1]
    else:
        if dados[1] >= ma:
            ma = dados[1]
        if dados[1] <= me:
            me = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input(' Quer continhar? [S/N] ')).strip().upper()[0]
    while r not in 'NS':
        r = str(input(' Quer continhar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-='*30)
print(f' Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f' O maior peso foi de {ma:.1f}kg. Peso de:', end=' ')
for c in pessoas:
    if c[1] == ma:
        print(f'{c[0]}', end=' ')
print( )
print(f' O menor peso foi de {me:.1f}kg. Peso de:', end=' ')
for c in pessoas:
    if c[1] == me:
        print(f'{c[0]}', end=' ')
print( )
