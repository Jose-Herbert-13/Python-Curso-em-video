v = float(input(' Qual a velocidade do carro:(km/h) '))
if v>80:
    n = (v-80)*7
    print(' Você ultrapassou o limite de velocidade e foi multado com uma multa de R${:.2f}'.format(n))
print(' Tenha um bom dia, dirija com segurança')
