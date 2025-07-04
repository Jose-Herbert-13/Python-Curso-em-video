print('-='*13)
print(' ANALISADOR DE TRIÂNGULOS ')
print('-='*13)
a = float(input(' Primeiro segmento: '))
b = float(input(' Segundo segmento: '))
c = float(input(' Terceiro segmento: '))
if a<b+c and b<a+c and c<a+b:
    t = 'PODEM FORMAR'
else:
    t = 'NÃO PODEM FORMAR'
print(' Esses segmentos {} um triângulo'.format(t))