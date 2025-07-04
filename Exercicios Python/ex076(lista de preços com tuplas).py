p = ('Caderno', '27.50', 
        'Canetas', '5.00', 
        'Lápis', '1.50', 
        'Borrachas', '1.50', 
        'Estojo', '12.50', 
        'Mochila', '149.99', 
        'Livro', '36.99', 
        'Fone Bluetooth', '60.00', 
        'Ps5', '6000.00')
print('-'*38)
print(f'{"Lista de Compras":^38}')
print('-'*38)
for c in range(0, len(p), 2):
    print(f' {p[c]:.<25} R${p[c+1]:>7}')
print('-'*38)
