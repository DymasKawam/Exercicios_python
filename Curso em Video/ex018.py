import math
ang = float(input('Digite o angulo que você deseja: '))
Seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tange = math.tan(math.radians(ang))  
print('O Angulo de {} tem o SENO de {:.2f}'.format(ang, Seno))
print('O Angulo de {} tem o COSSENO de {:.2f}'.format(ang, coss))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tange))