frase = str(input(' Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(' Temos um palídromo!')
else:
    print(' A frase digitada não é um palídromo!')