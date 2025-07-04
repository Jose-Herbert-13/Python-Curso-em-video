from math import hypot
co = float(input(' Qual a medida do cateto oposto? '))
ca = float(input(' Qual a medida do cateto adjacente? '))
hp = hypot(co, ca)
print(' A medida da hipotenusa é {:.2f}'.format(hp))