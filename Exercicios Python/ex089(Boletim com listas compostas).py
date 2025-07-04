boletim = []
aluno = []
nota = []
m = s = 0
while True:
    aluno.append(str(input(' Nome: ')).strip())
    for c in range(1,3):
        nota.append(float(input(f' Nota {c}: ')))
    aluno.append(nota[:])
    for c in nota:
        s += c
    m = s/2
    s = 0
    aluno.append(m)
    boletim.append(aluno[:])
    nota.clear()
    aluno.clear()
    r = str(input(' Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'NS':
        r = str(input(' Quer continuar? [S/N] ')).strip().upper()[0]
    if r=='N':
        break    
print('-='*30)
print(f" N°  {'Nome':<15} Média")
print('-'*26)
for c, v in enumerate(boletim):
    print(f' {c}  {v[0]:<15} {v[2]}')
print('-'*26)
while True:
    n = int(input(' Mostrar notas de qual aluno? (999 interrompe): '))
    if n==999:
        print(' FINALIZANDO...')
        break
    elif n<len(boletim):
        print(f' Notas de {boletim[n][0]}: {boletim[n][1]}')
    else:
        print(' Opção invalida')
print(' >>> Volte Sempre <<< ')
