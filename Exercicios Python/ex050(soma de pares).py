s = 0
q = 0
for c in range(1, 7):
    n = int(input(' Digite o {}° valor: '.format(c)))
    if n%2==0:
        s += n
        q += 1
print(' Você informou {} valores pares e a soma deles é {}'.format(q, s))