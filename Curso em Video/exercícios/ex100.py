'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
from random import randint
from time import sleep
números = []
def sorteia():
    print('-=' * 20)
    print('Sorteando Os valores: ', end='')
    for c in range(1,6):
        radom = randint(1,10)
        números.append(radom)
        print(radom, end=' ', flush= True)
        sleep(0.3)
    print()

def somaPar():
    print('-=' * 20)
    pares = 0
    print(f'Somando os valores pares de {números}: ', end='')
    for par in números:
            if par % 2 == 0:
                 pares += par
    print(f'São {pares}')      
    print('-=' * 20)
sorteia()
somaPar()