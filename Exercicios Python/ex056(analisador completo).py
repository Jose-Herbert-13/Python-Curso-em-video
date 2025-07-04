total = 0
hmv = 0
tm20 = 0
for c in range(1, 5):
    print(' ----- {}° Pessoa -----'.format(c))
    nome = str(input(' Nome: ')).strip()
    idade = int(input(' Idade: '))
    sexo = str(input(' Sexo [M/F]: ')).strip().upper()
    total += idade
    if sexo=='M' and idade>hmv:
        mvn = nome
        mvi = idade
    if sexo=='F' and idade<20:
        tm20 += 1
m = total/4
print(' A média de idade do grupo é de {} anos \n O homem mais velho tem {} anos e se chama {} \n E ao todo {} mulheres são menores de 20 anos'.format(m, mvi, mvn, tm20))
