boletim = {}
boletim['Nome'] = str(input(' Nome: '))
boletim['Média'] = float(input(f' Média de {boletim["Nome"]}: '))
if boletim['Média'] < 5:
    boletim['Situação'] = 'Reprovado'
elif boletim['Média'] < 7:
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Aprovado'
print('-='*35)
for k, v in boletim.items():
    print(f' {k} é igual a {v} ')
