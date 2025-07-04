from ex107 import moeda

n = float(input(' Digite um valor: R$'))
print(f' A metade de R${n:.2f} é R${moeda.metade(n):.2f}')
print(f' O dobro de R${n:.2f} é R${moeda.dobro(n):.2f}')
print(f' Aumentando 13% fica: R${moeda.aumentar(n, 13):.2f}')
print(f' Diminuindo 10% fica: R${moeda.diminuir(n, 10):.2f}')
