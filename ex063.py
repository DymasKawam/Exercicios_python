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
'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
nú = int(input('Digite um número: '))
con = 'S'
maior = menor = soma = nú
div = cont = 1
while con != 'N':
    con = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if con == 'S':
        nú = int(input('Digite um número: '))
        soma += nú
        div += 1
        cont += 1
        if maior < nú:
            maior = nú
        if menor > nú:
            menor = nú 
    if con != str and con != 'S' and con != 'N':
        while con != 'S' and con != 'N' and con != str:
            print('erro digite S para continuar e N para parar o programa.')
            con = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
média = soma / div
print('Você contou {} números e a média foi {:.2f}'.format(cont,média))
print('O maior número foi {} e o menor {}.'.format(maior,menor))