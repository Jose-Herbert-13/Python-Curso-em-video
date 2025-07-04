def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31m ERRO! Por favor, digite um número inteiro valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m O usuario optou por não digitar o valor\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f' \033[33m{c}\033[m -- \033[36m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint(' \033[33mSua Opção: \033[m')
    return opc


