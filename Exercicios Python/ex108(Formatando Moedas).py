from ex108 import moeda

n = float(input(' Digite um valor: R$'))
print(f' A metade de {moeda.moeda(n)} é R${moeda.moeda(moeda.metade(n))}')
print(f' O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f' Aumentando 13% fica: {moeda.moeda(moeda.aumentar(n, 13))}')
print(f' Diminuindo 10% fica: {moeda.moeda(moeda.diminuir(n, 10))}')
