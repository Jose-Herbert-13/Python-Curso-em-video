n1 = float(input(' Digite sua primeira nota: '))
n2 = float(input(' Digite sua segunda nota: '))
n3 = float(input(' Digite sua terceira nota: '))
n4 = float(input(' Digite sua quarta nota: '))
m = (n1+n2+n3+n4)/4
print(' Sua média nessas 4 notas foi {:.1f}'.format(m))
if m<5: 
    print(' Você está reprovado')
elif m<=7: # 7 > m >= 5
    print(' Você está de recuperação')
else:  # elif m >= 7
    print(' Você está aprovado')
