'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''


lista = []
v = 0

while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Número ja adicionado. tente novamente.')
        continue
    lista.append(num)
    v += 1
    conti = str(input('Deseja continuar?: ')).strip()
    if conti in 'Nn':
        break

lista.sort()
print(lista)