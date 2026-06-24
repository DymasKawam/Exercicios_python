'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número inteiro: ')))
        #vai separara os números pares dos impares e colocalos nas suas repectivas listas   
    conti = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while conti not in 'SsNn':
        print('Valor INVALIDO!!! Digite apenas "S" para sim ou "N" para não.')
        conti = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if conti in 'Nn':
        break

#Vai perguntar os números e colocar na lista principal.
for i, v in enumerate (lista): 
        if v % 2 == 0:
            pares.append(lista[i])
        if v % 2 != 0:
            impares.append(lista[i]) 
print(f'A lista completa é: {lista}')
print(f'Os pares dessa lista são: {pares}')
print(f'Os impares dessa lista são: {impares}')