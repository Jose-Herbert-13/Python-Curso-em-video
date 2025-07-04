frase = str(input(' Digite uma frase: ')).lower().strip()
print(" A letra 'a' aparece {} vezes na frase".format(frase.count("a")))
print(' A primeira vez q ela aparece é na posição {}'.format(frase.find("a")+1))
print(' A última vez que ela aparece é na posição {}'.format(frase.rfind("a")+1))