from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f' Os números sorteados foram: ', end='')
for e in n:
    print(e, end=' ')
print(f'\n O maior número é: {max(n)}')
print(f' O menor número é: {min(n)}')
