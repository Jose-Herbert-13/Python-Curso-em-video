s = q = 0
n = int(input(' Digite um número [999 para parar]: '))
while n != 999:
        s += n
        q += 1
        n = int(input(' Digite um número [999 para parar]: '))
print(' Você digitou {} números e a soma deles foi {}'.format(q, s))