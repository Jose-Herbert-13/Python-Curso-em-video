preço = float(input(' Qual o valor da casa que você quer comprar? R$'))
salario = float(input(' Qual o seu salário? R$'))
tempo = int(input(' Em quantos anos você pretende pagar? '))
mensal = preço/(tempo*12)
x = salario*0.3
print(' Para pagar uma casa de {} em {} ano(s) \n você terá que pagar R${:.2f} por mês'.format(preço, tempo, mensal))
if mensal <= x:
    print(' Empréstimo Pode Ser Concedido')
else:
    print(' Empréstimo Negado')
