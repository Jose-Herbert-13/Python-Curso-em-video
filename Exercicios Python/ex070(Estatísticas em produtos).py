mil = q = t = 0
print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)
while True:
    nome = str(input(' Nome do produto: ')).strip()
    preço = float(input(' Preço: R$'))
    q += 1
    t += preço
    if q == 1 or preço < me:
        me = preço
        mnome = nome
    if preço > 1000:
        mil += 1
    r = str(input(' Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'NS':
        r = str(input(' Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break
print('-'*30)
print('{:-^30}'.format('FIM DO PROGRAMA'))  
print(f' O preço total da compra foi R${t:.2f} \n Temos {mil} produtos custando mais de R$1000.00 \n o produto mais barato foi {mnome} que custa R${me:.2f}')
