'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
matriz = []
jogos = int(input('Digite quantos jogos serão jogados: '))
for c in range(0, jogos ):
    matriz.append([])
    for sor in range(0,6):
        matriz[c].append(randint(1,60))
    sleep(1)
    print(f'jogo {c + 1}: {matriz[c]}')
    