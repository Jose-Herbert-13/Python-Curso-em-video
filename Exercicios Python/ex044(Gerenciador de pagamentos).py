print('\033[31m', '='*7, 'Loja Anime', '='*7, '\033[m')
valor = float(input(' Qual o valor do produto? R$'))
print(''' \033[7;31mEscolha o tipo de pagamento:\033[m
  \033[2m [1] À Vista(Dinheiro ou Cheque)\033[m
  \033[2m [2] À Vista no Cartão\033[m')
  \033[2m [3] 2x no Cartão\033[m')
  \033[2m [4] 3x ou Mais no Cartão\033[m''')
tipo = int(input(' '))
if tipo == 1:
    vn = valor*0.9
    print(' Você terá 10% de desconto então pagará um total de R${:.2f}'.format(vn))
elif tipo == 2:
    vn = valor*0.95
    print(' Você terá 5% de desconto então pagará um total de R${:.2f}'.format(vn))
elif tipo == 3:
    m = valor/2
    print(' Você pagará R${:.2f} dividido para 2 vezes \n Que dá um valor de R${:.2f} por mês'.format(valor, m))
elif tipo == 4:
    p = int(input(' Digite a quantidade de parcelas que você deseja: '))
    vn = valor*1.2
    m = vn/p
    print(' Você pagará 20% de juros que dá um total de R${:.2f} \n Dividido para {} vezes, que dá um valor de R${:.2f} por mês'.format(vn, p, m))
else:
    print(' \033[41mOpção de pagamento inválida\033[m')