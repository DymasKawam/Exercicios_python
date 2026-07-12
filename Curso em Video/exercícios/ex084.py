'''Exercício Python 084: Faça um programa que leia nome e peso de vária Pessoas, guardando tudo em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais Pesadas.
C) Uma listagem com as pessoas mais leves.'''

maior = menor = 0 
cont = ''
pessoa = []
dados_pessoas = []
mesmo_pesoM = []
mesmo_pesoN = []



#Pega os dados das pessoas e coloca em uma lista
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    while True:
        cont = str(input('Deseja continuar?[S/N]: '))
        if cont in 'SsNn':
            break
        else:
            print('Valor inválido!!! Digite novamente.')
    if cont in 'Nn':
        break

#Aqui ele navega pela lista pessoa e coloca os dados delas separados em uma lista chamada dados_pessoas
for c in range (0, len(pessoa), 2):
    i = c + 2
    dados_pessoas.append(pessoa[c:i])

#Vai separar a pessoa mais pesada e da menos pesada
for c in range (0, len(dados_pessoas)):
    if c == 0:
        maior = menor = dados_pessoas[c][1]
    else:
        if dados_pessoas[c][1] > maior:
            maior = dados_pessoas[c][1]
            nomeM = dados_pessoas[c][0]
        if dados_pessoas[c][1] < menor:
            menor = dados_pessoas[c][1]
            nomeN = dados_pessoas[c][0]

            
#Ele vai pegar o nome das pessoas que tem mesmo peso.
for c in range (0, len(dados_pessoas)):
    if dados_pessoas[c][1] == maior:
        mesmo_pesoM.append(dados_pessoas[c][0])
    if dados_pessoas[c][1] == menor:
        mesmo_pesoN.append(dados_pessoas[c][0])

#Aqui vai mostrar os dados das pessoas na tela
print(f'Foram cadastradas {len(dados_pessoas)} pessoas.')
print(f'O maior peso foi de {maior}. De {mesmo_pesoM}.')
print(f'O menor peso foi de {menor}. De {mesmo_pesoN}')