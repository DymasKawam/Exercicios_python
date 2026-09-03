'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''

idade_total = 0
lista = []
dados = {}
pessoas_total = média = 0 
while True:
    nome = str(input('Nome: ')).strip().title()
    sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]
    if sexo not in 'MmFf':
        while sexo not in 'MmFf':
            print('Erro! digite somente M para masculino e F para feminino.')
            sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    idade_total += idade
    dados['nome'] = nome
    dados['sexo'] = sexo
    dados['idade'] = idade
    lista.append(dados.copy())

    pessoas_total += 1
    cont = str(input('Deseja continuar?[S/N]: ')).strip()
    if cont not in 'SsNn':
        while cont not in 'SsNn':
            print('Erro! Digite somente "S" para sim e "N" para não.')
            cont = str(input('Deseja continuar?[S/N]: ')).strip()
    if cont in 'Nn':
        break
média = idade_total // pessoas_total
print('-=' * 30)
print(f'A: Ao todo tem {pessoas_total} pessoas cadastradas.')
print(f'B: A média de idade é {média:5.2f}')

print('C: As mulheres cadastradas foram: ',end= '')
for d in lista:
    if d['sexo'] == 'F':
        print(d['nome'], end='. ')
print()
print('D: Lista de pessoas que estão acima da média: ')
for D in lista:
    if D['idade'] > média:
        print(f'nome = {D['nome']}; sexo = {D['sexo']}; idade = {D['idade']}')
print('== ACABOU ==')
