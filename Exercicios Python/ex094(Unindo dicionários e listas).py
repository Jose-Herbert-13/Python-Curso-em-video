lista = []
pessoas = {}
s = m = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input(' Nome: '))
    pessoas['Sexo'] = str(input(' Sexo? [M/F] ')).upper().strip()[0]
    while pessoas['Sexo'] not in 'MF':
        print(' ERRO! Digite apenas M ou F.')
        pessoas['Sexo'] = str(input(' Sexo? [M/F] ')).upper().strip()[0]
    pessoas['Idade'] = int(input(' Idade: '))
    s += pessoas['Idade']
    lista.append(pessoas.copy())
    r = str(input(' Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'NS':
        print(' ERRO! Digite apenas S ou N.')
        r = str(input(' Quer continuar? [S/N] ')).upper().strip()[0]
    if r=='N':
        break
m = s/len(lista)
print('-='*35)
print(f' -- O grupo tem {len(lista)} pessoas.')
print(f' -- A média de idade é de {m:.2f} anos.')
print(' -- As mulheres cadastradas foram: ', end='')
for v in lista:
    if v['Sexo'] == 'F':
        print(v['Nome'], end=' ')
print() 
print(' -- Lista de pessoas com idade acima da média: ')
print()
for v in lista:
    if v['Idade'] > m:
        print('    ', end='')
        for k, c in v.items():
            print(f' {k} = {c}', end='; ')
        print()
print(' << ENCERRADO >> ')
