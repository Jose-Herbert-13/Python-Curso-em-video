def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada=='':
            print(f'\033[31m Erro! "{entrada}" é invalido\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(txt):
    while True:
        num = input(txt)
        if num.isnumeric():
            break
        print('\033[31m ERRO! Digite um número inteiro válido\033[m')
    return num


