def notas(*nota, sit=False):
    """
    --> Função para analisar notas de vários alunos:
        n = notas
        sit = parametro opcional para mostrar a situação, por padrão esta desativado
        return = dicionario com todos os dados
    """
    boletim = dict()
    maior = menor = s = m = 0
    boletim['Total'] = len(nota)
    boletim['Maior'] = max(nota)
    boletim['Menor'] = min(nota)
    boletim['Média'] = sum(nota)/len(nota)
    if sit==True:
        if boletim['Média']>=7:
            boletim['Situação'] = 'Boa'
        elif boletim['Média']>=5:
            boletim['Situação'] = 'Razoavel'
        else:
            boletim['Situação'] = 'Ruim'
    return boletim


r = notas(9.8, 6.9, 7.0, sit=True)
for k, v in r.items():
    print(f' {k}: {v}')
