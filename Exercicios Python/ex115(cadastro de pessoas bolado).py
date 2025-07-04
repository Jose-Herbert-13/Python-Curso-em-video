from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'
if arquivoExiste(arq):
    print(' Arquivo encontrado com sucesso!')
else:
    print(' Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do programa'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input(' Nome: '))
        idade = leiaint(' Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do Sistema -- Até logo')
        break
    else:
        print('\033[31m ERRO! Digite uma opção valida\033[m')
    sleep(1)
    
