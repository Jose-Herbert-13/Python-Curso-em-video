def metade(m=0):
    m *= 0.5
    return moeda(m)


def dobro(d=0):
    d *= 2
    return moeda(d)


def aumentar(a=0, t=0):
    a += a*(t/100)
    return moeda(a)


def diminuir(di=0, p=0):
    di -= di*(p/100)
    return moeda(di)


def moeda(n=0, m='R$'):
    return f"{m}{n:.2f}".replace('.', ',')


def resumo(preço=0, aumento=0, diminuiçao=0):
    print('-'*33)
    print('RESUMO DO VALOR'.center(33))
    print('-'*33)
    print(f' Preço analisado: \t{moeda(preço)}')
    print(f' Dobro do valor: \t{dobro(preço)}')
    print(f' Metade do valor: \t{metade(preço)}')
    print(f' Aumentando {aumento}%: \t{aumentar(preço, aumento)}')
    print(f' Diminuindo {diminuiçao}%: \t{diminuir(preço, diminuiçao)}')
    print('-'*33)


