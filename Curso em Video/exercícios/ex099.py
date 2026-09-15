'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(*num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    maior = 0
    cont = 0
    for c in num:
        if len(num) == 1 and num[0] == 0:
            break 
        print(f'{c} ', end='')
        if cont == 0:
            maior = c 
        else:
            if  maior < c:
                maior = c
        cont += 1
    if len(num) == 1 and num[0] == 0:
        print(f'Foram informados 0 valores ao todo.')
    else:
        print(f'Foram informados {len(num)} valores ao todo.')
    print()
    print(f'O maior valor informado foi {maior}')
    print('-=' * 20)


maior(2, 9, 4, 5, 7, 1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()