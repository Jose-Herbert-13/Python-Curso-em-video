def voto(nasc):
    """
    --> calcula a idade e diz se a pessoa pode ou não votar, sendo:
        nasc = ano de nascimento
    """
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f' Com {idade} anos, não pode votar' 
    elif idade<18 or idade >= 65:
        return f' Com {idade} anos, o voto é Opcional'
    else:
        return f' Com {idade} anos, o voto é Obrigatório'

print('-'*30)
print(voto(int(input(' Em que ano você nasceu? '))))
