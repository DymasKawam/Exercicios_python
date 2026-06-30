'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
'A variavel peso vai contar o peso da pessoa'

'Criando as variaveis que vao receber filtrar o maior e o menor peso'
maior_peso = 0 
menor_peso = 0
'O estrutura de repetição for vai fazer da pessoa 1 ate a 6'
for pess in range (1,6):
    'Aqui a variavel que vai perguntar o peso'
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pess)))
    'A estrutura vai adicionar o maior peso e o menor peso'
    if pess == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior peso lido foi o {:.1f}'.format(maior_peso))
print('O menor peso lido foi {:.1f}'.format(menor_peso))