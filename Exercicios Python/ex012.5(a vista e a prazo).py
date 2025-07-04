v = float(input(' Qual o valor do pagamento? '))
p = float(input(' Vai dividir em quantas parcelas?(caso seja a vista digite 0) '))
vt = v + v*(0.03*p)
print(' O valor a ser pago será de R${}, e caso seja parcelado será o valor total pelo numero de parcelas por mês'.format(vt))