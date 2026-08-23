'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}

print('Jogando os dados:')
for c in range (1,5):
    dado = randint(1,6)
    jogadores[f'jogador {c}'] = dado
    print(f'    jogador {c} = {dado}')
    sleep(1)

ranking = {}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
posição = 1
print('Vencedores:')
for c in range(0,len(ranking)):
    print(f'    {posição}º lugar {ranking[c][0]}: {ranking[c][1]} ')
    posição += 1
    sleep(1)