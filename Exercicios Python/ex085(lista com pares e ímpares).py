lista = [[], []]
for c in range(1, 8):
    n = int(input(f' Digite o {c}° valor: '))
    if n%2==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f' Os valores Pares digitados foram: {lista[0]}')
print(f' Os valores Ímpares digitados foram: {lista[1]}')
