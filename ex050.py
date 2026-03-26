'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
com = 0 
s = 0 
for c in range (1,7):
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        com = com + 1
        s = s + num
print('A soma dos números pares são {} e a quantidade de números pares são {}.'.format(s, com))