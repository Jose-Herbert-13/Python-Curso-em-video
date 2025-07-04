sa = float(input(' Qual o salário do funcionário? R$'))
if sa<=1250.00:
    novo = sa*1.15
else:
    novo = sa*1.10
print(' Quem ganhava R${:.2f}, terá um novo salário de: R${:.2f}'.format(sa, novo))
