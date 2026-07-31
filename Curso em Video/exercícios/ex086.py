'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[], [], []]
valor = l = c = 0
for i in range (0,9):  
    valor = int(input(f'Digite o valor no [{c}, {l}]: '))
    l += 1
    if c == 0:
        matriz[0].append(valor)
    elif c == 1:
        matriz[1].append(valor)
    elif c == 2:
        matriz[2].append(valor)
    if l > 2:
        c += 1 
        l = 0
l = c = 0
while True:
    
    print(f'[{matriz[c][l]:^5}]', end='')
    l += 1
    if l > 2:
        print()
        c += 1 
        l = 0
    if c > 2:
        break