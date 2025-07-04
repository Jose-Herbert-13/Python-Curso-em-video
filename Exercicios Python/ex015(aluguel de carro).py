d = int(input(' Por quantos dias o carro foi alugado? '))
km = float(input(' Quabtos km foram rodados? '))
p = d*60+km*0.15
print(' O total a pagar por ter alugado o carro será de R${:.2f}'.format(p))