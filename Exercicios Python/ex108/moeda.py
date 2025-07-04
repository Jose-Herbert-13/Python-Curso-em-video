def metade(n=0):
    n *= 0.5
    return n


def dobro(n=0):
    n *= 2
    return n


def aumentar(n=0, t=0):
    n += n*(t/100)
    return n


def diminuir(n=0, t=0):
    n -= n*(t/100)
    return n


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')


