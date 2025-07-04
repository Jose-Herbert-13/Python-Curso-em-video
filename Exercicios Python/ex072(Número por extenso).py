extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input(' Digite um número entre 0 e 20: '))
    while n<0 or n>20:
        n = int(input(' Tente novamente. Digite um número entre 0 e 20: '))
    print(f' Você digitou o número {extenso[n]}.')
    r = str(input(' Você quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'NS':
        r = str(input(' Tente novamente. Você quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print(' Volte Sempre')