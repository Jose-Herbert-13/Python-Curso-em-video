def área(l, c):
    """
    --> Calcula a área de um terreno, sendo:
        l = largura
        c = comprimento
    """
    print(f' A área de um terreno de {l}×{c} é {l*c}m².')


print('-'*30)
print(f"{'CONTROLE DE TERRENOS':^30}")
print('-'*30)
área(float(input(' LARGURA (m): ')), float(input(' COMPRIMENTO (m): ')))
