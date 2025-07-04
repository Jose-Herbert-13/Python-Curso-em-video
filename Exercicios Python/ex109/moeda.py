def metade(m=0, formato=False):
    m *= 0.5
    return m if formato is False else moeda(m)


def dobro(d=0, formato=False):
    d *= 2
    return d if formato is False else moeda(d)


def aumentar(a=0, t=0, formato=False):
    a += a*(t/100)
    return a if formato is False else moeda(a)


def diminuir(di=0, p=0, formato=False):
    di -= di*(p/100)
    return di if formato is False else moeda(di)


def moeda(n=0, m='R$'):
    return f"{m}{n:.2f}".replace('.', ',')


