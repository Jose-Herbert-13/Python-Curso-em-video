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


def leiafloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31m ERRO! Por favor, digite um número real valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m O usuario optou por não digitar o valor\033[m')
            return 0
        else:
            return num


n = leiaint(' Digite um número inteiro: ')
r = leiafloat(' Digite um número Real: ')
print(f' Você digitou os números {n} e {r}')
