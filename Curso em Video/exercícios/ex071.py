'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('=' * 60)
print(f'{"Caixa Eletrônico":^60}')
print('-' * 60)
sacar = int(input('Digite o valor a ser sacado: R$'))
print('-' * 60)
if (sacar // 50) > 0:
    nota50 = sacar // 50
    sacar -= nota50 * 50
    print(f'Total de {nota50} cedulas de R$50')
if (sacar // 20)> 0:
    nota20 = sacar // 20
    sacar -= nota20 * 20
    print(f'Total de {nota20} cedulas de R$20')
if (sacar // 10) > 0:
    nota10 = sacar // 10
    sacar -= nota10 * 10
    print(f'Total de {nota10} cedulas de R$10')
if (sacar // 1 ) > 0:
    nota1 = sacar // 1
    sacar = nota1
    print(f'Total de {nota1} cedulas de R$1')
print('=' * 60)