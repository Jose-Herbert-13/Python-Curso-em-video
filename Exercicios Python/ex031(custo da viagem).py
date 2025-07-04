km = float(input(' Qual a distancia em km da viagem? '))
print(' Você está prestes a começar um viagem de {:.2f}km'.format(km))
if km<=200:
    p = km*0.5
else:
    p = km*0.45
# p = km*0.5 if km<=200 else km*0.45
print(' e você terá que pagar: R${:.2f}'.format(p))