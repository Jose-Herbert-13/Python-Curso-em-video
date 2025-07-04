fut = {}
gol = []
t = 0
fut['Nome'] = str(input(' Nome do jogador: '))
q = int(input(f' Quantas partidas {fut["Nome"]} jogou? '))
for c in range(0, q):
    gol.append(int(input(f' Quantos gols na partida {c+1}? ')))
fut['Gols'] = gol
fut['Total'] = sum(gol)
print('-='*35)
print(fut)
print('-='*35)
for k, v in fut.items():
    print(f' O campo {k} tem o valor {v}')
print('-='*35)
print(f' O jogador {fut["Nome"]} jogou {len(fut["Gols"])} partidas.')
for c, v in enumerate(fut['Gols']):
    print(f'     => Na partida {c+1}, fez {fut["Gols"][c]}.')
print(f' Foi um total de {fut["Total"]} gols.')
