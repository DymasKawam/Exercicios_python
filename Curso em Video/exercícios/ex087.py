'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
soma = somaC = maior = 0
matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o número na posição [{l},{c}]: ')))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    if matriz[1]:
        for i in range(len(matriz[1])):
            if matriz[1][i] > maior:
                maior = matriz[1][i]
    somaC += matriz[l][2] 
print('-='* 30)
l = c = 0
while True:
    print(f'[{matriz[l][c]:^5}]', end='')
    c += 1
    if c > 2:
        print()
        l += 1
        c = 0
    if l > 2:
        break
print('-=' * 30)
print(f'A soma de todos os valores pares digitados foram: {soma}')
print(f'A soma dos valores da terceira coluna foram: {somaC}')
print(f'O maior valor da segunda linha: {maior}')