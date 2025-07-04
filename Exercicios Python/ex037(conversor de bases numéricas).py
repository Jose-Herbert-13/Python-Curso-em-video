n = int(input(' Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão: \033[2m 
 [1] Binário
 [2] Octal
 [3] Hexadecimal
\033[m''')
r = int(input(' '))

if r == 1:
    print(' {} convertido para Binário é igual à {}'.format(n, bin(n)[2:]))
elif r == 2:
    print(' {} convertido para Octal é igual à {}'.format(n, oct(n)[2:]))
elif r == 3:
    print(' {} convertido para Hexadecimal é igual à {}'.format(n, hex(n)[2:]))
else:
    print(' Essa opção não está disponível. Tente novamente.')
