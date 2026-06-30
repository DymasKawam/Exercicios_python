'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, inde de 10 até 0 com uma pausa de 1 segundo entre elas'''
from time import sleep
print('-=' * 20)
print('Contagem para os fogos de artifícios')
print('-=' * 20)
for c in range(10,0, -1):
    sleep(1)
    print(c)
print('fim')