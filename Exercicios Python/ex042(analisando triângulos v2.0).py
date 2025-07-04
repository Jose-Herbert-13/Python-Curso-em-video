print('\033[2;35m')
print('-='*13)
print(' ANALISADOR DE TRIÂNGULOS ')
print('-='*13)
print('\033[m')
a = float(input(' Primeiro segmento: '))
b = float(input(' Segundo segmento: '))
c = float(input(' Terceiro segmento: '))
if a<b+c and b<a+c and c<a+b:
    t = 'PODEM FORMAR'
    if a == b == c:
        ti = 'EQUILÁTERO'
    elif a != b != c != a:
        ti = 'ESCALENO'
    else:  #(a==b or b==c or a==c) and (a!=b or a!=c or b!=c)
        ti =  'ISÓSCELES'
else:
    t = 'NÃO PODEM FORMAR'
    ti = ' '
print(' Esses segmentos {} um triângulo {}'.format(t, ti))
