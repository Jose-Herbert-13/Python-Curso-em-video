from math import radians, sin, cos, tan
ang = float(input(' Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(' O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print(' O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
print(' O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))