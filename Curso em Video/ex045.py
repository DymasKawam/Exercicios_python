'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
from time import sleep
import random


print('''Suas opções:
      [0] pedra
      [1] papel
      [2] tesoura''')
jogada = int(input('Qual é a sua jogada?: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

computador = random.choice(['pedra', 'papel', 'tesoura'])
print(computador)
if jogada == 0:
    if computador == 'pedra':
        resultado = 'EMPATE'
    elif computador == 'papel':
        resultado = 'JOGADOR VENCE'
    else:
        resultado = 'JOGADOR PERDE'
elif jogada == 1:
    if computador == 'pedra':
        resultado = 'JOGADOR VENCE'
    elif computador == 'papel':
        resultado = 'EMPATE'
    else:
        resultado = 'JOGADOR PERDE'
elif jogada == 2:
    if computador == 'pedra':
        resultado = 'JOGADOR PERDE'
    elif computador == 'papel':
        resultado = 'JOGADOR GANHA'
    else:
        resultado = 'EMPATE'
if jogada == 0:
    jogada = 'pedra'
elif jogada == 1:
    jogada = 'papel'
elif jogada == 2:
    jogada = 'tesoura'
print('''{} 
Computador jogou {}
jogador jogou {}
{}'''.format('-=' * 10, computador, jogada, '-=' * 10 ))
print('resultador é {}'.format(resultado))