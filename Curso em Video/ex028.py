from random import randrange
from time import sleep
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
n = int(input('Em que número eu pensei?: '))
c = randrange(5)
print('PROCESANDO...')
sleep(2)
if n == c:
    print('PARABÉNS. Você conseguiu me vencer')
else:
    print('Ganhei. Eu pensei no número {}'.format(c))