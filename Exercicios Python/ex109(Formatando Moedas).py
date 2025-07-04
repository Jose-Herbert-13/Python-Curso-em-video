from ex109 import moeda

n = float(input(' Digite um valor: R$'))
print(f' A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f' O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f' Aumentando 13% fica: {moeda.aumentar(n, 13, True)}')
print(f' Diminuindo 10% fica: {moeda.diminuir(n, 10, True)}')
