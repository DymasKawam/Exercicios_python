'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def área(l, c):
    res = l * c
    print(f'A área de um terreno {l:.2f}x{c:.2f} é igual a {res:.2f}m²')

área(float(input('Largura: ')), float(input('Comprimento: ')))