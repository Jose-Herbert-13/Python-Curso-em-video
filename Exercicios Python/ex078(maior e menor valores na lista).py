valores = []
for c in range(0,5):
    valores.append(int(input(f' Digite um valor para a posição {c}: ')))
ma = max(valores)
me = min(valores)
print('-='*25)
print(f' Você digitou os valores: {valores}')
print(f' O maior valor digitado foi {ma} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == ma:
        print(f'{c}...', end=' ')
print(f'\n O menor valor digitado foi {me} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == me:
        print(f'{c}...', end=' ')
