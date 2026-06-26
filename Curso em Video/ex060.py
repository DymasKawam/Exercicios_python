'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
n1 = int(input('Digite o seu número: '))
tot = 1
fato = n1
print('O fatorial de seu número é igual a: ')
while fato >= 1:
    print('{}'.format(n1), end='')
    print(' x ' if n1 > 1 else ' = ', end='')
    n1 -= 1
    tot *= fato 
    fato -= 1
print(tot)