def escreva(txt):
    """
    --> Faz um print organizado com linhas proporcionais a o tamanho da frase, sendo:
        txt = frase
    """
    tam = len(txt)+4
    print('~'*tam)
    print(f'  {txt}')
    print('~'*tam)


escreva('One Piece')
print()
escreva('Jojo Bizarre Adventure')
print()
escreva('Vai Tomar No Cu Genisson')