r = 'S'
me = ma = s = q = 0
while r in 'S':
    n = int(input(' Digite um número: '))
    s += n
    q += 1
    if me == 0:
        me = n
    if n < me:
        me = n
    if n > ma:
        ma = n
    r = str(input(' Deseja continuar?[S/N] ')).strip().upper()[0]
m = s/q
print(' Você digitou {} valores e a média entre eles é {:.2f} \n O maior valor digitado foi {} e o menor foi {}'.format(q, m, ma, me))
