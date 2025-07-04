jogadores = []
fut = {}
gol = []
while True:
    gol.clear()
    fut.clear()
    print('-'*30)
    fut['Nome'] = str(input(' Nome do jogador: '))
    q = int(input(f' Quantas partidas {fut["Nome"]} jogou? '))
    for c in range(0, q):
        gol.append(int(input(f'     Quantos gols na partida {c+1}? ')))
    fut['Gols'] = gol[:]
    fut['Total'] = sum(gol)
    jogadores.append(fut.copy())
    r = str(input(' Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'NS':
        r = str(input(' Quer continuar? [S/N] ')).upper().strip()[0]
    if r=='N':
        break
print('-='*35)
print(f" Cod", end=' ')
for k in fut.keys():
    print(f'{k:<20}', end='')
print()
print('-'*70)
for c, v in enumerate(jogadores):
    print(f'{c:>4}', end=' ')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-'*70)
while True:
    n = int(input(' Mostras dados de qual jogador? [999 para] '))
    if n==999:
        break
    elif n<len(jogadores):
        print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[n]["Nome"]}:')
        for c, v in enumerate(jogadores[n]['Gols']):
            print(f'    No jogo {c+1} fez {v} gols.')
    else:
        print(f' Não existe jogador com o código {n}. Tente novamente')
    print('-'*70)
print(' >>>> VOLTE SEMPRE <<<< ')
