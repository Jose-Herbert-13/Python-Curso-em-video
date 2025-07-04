from random import shuffle
n1 = str(input(' Digite o nome do 1° aluno(a): '))
n2 = str(input(' Digite o nome do 2° aluno(a): '))
n3 = str(input(' Digite o nome do 3° aluno(a): '))
n4 = str(input(' Digite o nome do 4° aluno(a): '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(' A ordem de apresentação será: ')
print(" ", lista)