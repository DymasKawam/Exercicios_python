'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('os números sorteados foram: ',end='')
for cont in range (1,6):
    sorteio = randint(num[0],num[-1])
    print(sorteio, end='.')
    if cont == 5:
        print('\n')
    if cont == 1:
        maior = sorteio
        menor = sorteio
    else: 
        if sorteio > maior:
            maior = sorteio
        if sorteio < menor:
            menor = sorteio

print(f'Maior número foi {maior}')
print(f'Menor número foi {menor}')