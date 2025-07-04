from datetime import date
ct = {}
ct['Nome'] = str(input(' Nome: '))
nasc = int(input(' Ano de nascimento: '))
ct['Idade'] = date.today().year - nasc
ct['CTPS'] = int(input(' Carteira de Trabalho (0 não tem): '))
if ct['CTPS'] != 0:
    ct['Contratação'] = int(input(' Ano de contratação: '))
    ct['Salário'] = float(input(' Salário: R$'))
    ct['Aposentadoria'] = (ct['Contratação'] + 35) - nasc
print('-='*35)
print(ct)
for k, v in ct.items():
    print(f' {k} tem o valor {v} ')
