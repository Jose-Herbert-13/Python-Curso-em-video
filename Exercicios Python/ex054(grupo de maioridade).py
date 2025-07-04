from datetime import date
anoatual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(' Qual o anoem que a {}° pessoa nasceu? '.format(c)))
    idade = anoatual - nasc
    if idade<21:
        totmenor += 1
    else:
        totmaior += 1
print(' nesse grupo de pessoas {} ainda não alcançaram a maior idade \n e {} já alcançaram'.format(totmenor, totmaior))