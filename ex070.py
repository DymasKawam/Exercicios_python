'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

print('=' * 60)
print(f'{"Loja Do guilherme":^60}')
print('=' * 60)
cont = soma = mais_mil = menor = 0
produto_mais_barato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Qual é o preço do produto: R$'))
    soma += preço
    cont += 1
    if preço > 1000:
        mais_mil += 1
    if cont == 1:
        menor = preço
        produto_mais_barato = nome
    else:
        if menor > preço:
            produto_mais_barato = nome
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''O total gasto na compra foi {soma:.2f}.
      {mais_mil} Produtos custam mais de R$1000 reais.
      O nome do produto mais barato é {produto_mais_barato}''')