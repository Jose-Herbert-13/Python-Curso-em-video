for c in range(1, 6):
    peso = float(input(' Peso da {}° pessoa? '.format(c)))
    if c==1:
        menor = peso
        maior = peso
    else:
        if peso>maior:
            maior = peso
        if peso<menor:
            menor = peso
print(' O maior peso lido foi {:.1f}kg \n E o menor peso lido foi {:.1f}kg'.format(maior, menor))