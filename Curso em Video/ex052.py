'Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'
nu = int(input('Digite um numero: '))
divisao = 0 
for c in range (1, nu + 1):
    if nu % c == 0:
        print('\33[32m', end=' ')
        divisao = divisao + 1
    else:
        print('\33[31m', end= ' ')
    print('{}'.format(c), end=' ')
print('\n\033[m0 O número {} foi divisível {} vezes.'.format(nu,divisao))
if divisao > 2:
    resultado = 'NÃO É PRIMO'
else:
    resultado = 'PRIMO'
print('E por isso ele é {}'.format(resultado))