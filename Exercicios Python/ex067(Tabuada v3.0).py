while True:
    n = int(input(' Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if n<0:
        break
    for c in range(1, 11):
        print(f' {n} × {c} = {n*c}')
    print('-'*35)
print(' PROGRAMA TABUADA ENCERRADO. Volte sempre')
