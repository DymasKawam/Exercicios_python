'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
lista = []
print('-=' * 30)
for c in range (0,5):
    num = int(input(f'Digite o número na posição {c}: '))
    lista.append(num)
    if c == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Na lista {lista}')
print(f'O maior número foi {maior} na posição: ', end='')
for c in range(0,len(lista)):
    if lista[c] == maior:
        print(c, end=' ')
print(f'\nO menor número foi {menor} na posição: ', end='')
for c in range(0, len(lista)):
    if lista[c] == menor:
        print(c, end=' ')
print('\n-=' * 30)