'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randrange
tentativa = 0
compnum = randrange (10)
print('-=' * 50)
print('JOGO DE ADIVINHAÇÃO!!! TENTE ADIVINHAR QUAL NÚMERO O COMPUTADOR PENSOU!')
print('-=' * 50)
jognum = int(input('Digite o número que o computador pensou de 1 a 10: '))
while compnum != jognum:
    if jognum > compnum:
        jognum = int(input('Menos... tente novamente: '))
    else:
        jognum = int(input('Mais... tente novamente:'))
    tentativa += 1
print('Parabens você acertou!!!! a sua quantidade de tentativas foi de {}'.format(tentativa))
