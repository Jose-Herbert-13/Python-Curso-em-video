matriz =[[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
s = s3 = ma = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f' Digite um valor para [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f' [ {matriz[l][c]} ]', end=' ')
        if matriz[l][c]%2==0:
            s += matriz[l][c]
    print( )
print('-='*30)
for l in range(0,3):
    s3 += matriz[l][2]
for c in range(0, 3):
    if c==0 or matriz[1][c]:
        ma = matriz[1][c]
print(f' A soma dos valores pares é {s}')
print(f' A soma dos valores da terceira coluna é {s3}')
print(f' O maior valor da segunda linha é {ma}')
