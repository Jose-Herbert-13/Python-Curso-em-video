from datetime import date
anoatual = date.today().year
ano = int(input(' Qual o ano do seu nascimento: '))
sex = int(input(''' Qual o seu Gênero? 
 [1] Masculino
 [2] Feminimo
 '''))
idade = anoatual - ano
if sex == 1:
    print(' Sua idade é {}'.format(idade))
    if idade == 18:
        print(' Vkcê deve se alistar Imediatamente')
    elif idade < 18:
        print(' Você ainda vai se alistar dq à {} ano(s)'.format(18-idade))
        print(' Seu alistamento será em {}.'.format(ano+18))
    else:
        print(' O tempo de se alistar passou a {} ano(s)'.format(idade-18))
        print(' Seu alistamento foi em {}.'.format(idade+18))
elif sex == 2:
    print(' Seu gênero é Feminino, \n Logo você não necessita fazer o alistamento militar')