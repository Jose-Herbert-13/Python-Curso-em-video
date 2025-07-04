peso = float(input(' Qual o seu peso? (kg) '))
altura = float(input(' Qual a sua altura? (m) '))
imc = peso / altura**2
if imc<18.5:
    status = 'Abaixo do Peso'
elif 18.5<=imc<25:
    status = 'com o Peso Ideal' 
elif 25<=imc<30:
    status = 'com Sobrepeso'    
elif 30<=imc<40:
    status = 'com Obesidade'
else:
    status = 'com Obesidade Mórbida'
print(' O seu Imc é: {:.2f}, e você está {}'.format(imc, status))
