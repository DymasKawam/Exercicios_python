'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8 '''

nu = int(input('Digite a quantidade de termos que você quer: '))
f1 = 0
f2 = 1
print('{} -> {} ->'.format(f1, f2),end='')
cont = 3
while cont <= nu:
    soma = f1 + f2 
    print(' {} -> '.format(soma), end='')
    f1 = f2
    f2 = soma
    cont += 1
print('fim')
