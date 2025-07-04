from datetime import date
anoatual = date.today().year
ano = int(input(' Digite seu ano de nascimento: '))
idade = anoatual-ano
print(' Sua idade é {} ano(s)'.format(idade))
if idade <= 9:
    cate = 'MIRIM'
elif idade <= 14:
    cate = 'INFANTIL'
elif idade <= 19:
    cate = 'JUNIOR'
elif idade <= 25:
    cate = 'SÊNIOR'
else:
    cate = 'MASTER'
print(' Classificação: {}'.format(cate)) 