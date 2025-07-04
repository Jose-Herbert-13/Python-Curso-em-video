palavras = ('curso', 'python', 'jojo', 'one', 'piece','blue', 'lock', 'herbert', 'animes', 'stardew', 'valley', 'progamador', 'futuro')
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos:', end=' ')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')
print('\n', '-'*40)
