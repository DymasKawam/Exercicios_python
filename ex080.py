'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lista = []
for c in range (1,6):
    val = int(input(f'Digite o {c}º número:'))
    if c == 1:
        lista.append(val)
    for i, v in enumerate (lista):
    if val == lista[-1]:
        print('adicionado no final da lista')