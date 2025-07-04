h = m = a18 = 0
sexo = r = ' '
while True:
    print('-'*30)
    print(' Cadastre Uma Pessoa ')
    print('-'*30)
    idade = int(input(' Idade: '))
    sexo = str(input(' Sexo [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input(' Sexo [M/F] ')).upper().strip()[0]
    if idade >= 18:
        a18 +=1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    print('-'*30)
    r = str(input(' Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'NS':
        r = str(input(' Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break
print('-'*30)
print('--------FIM DO PROGRAMA-------')
print(f' Total de pessoas com mais de 18 anos: {a18} \n Ao todo temos {h} Homens cadastrados \n E temos {m} Mulheres com menos de 20 anos')