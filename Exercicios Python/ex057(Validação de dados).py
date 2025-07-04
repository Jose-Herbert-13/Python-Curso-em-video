sexo = str(input(' Informe o seu Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input(' Dados invalídos. Por favor, Informe seu sexo: ')).strip().upper()[0]
print(' Sexo {} registrado com sucesso'.format(sexo))
