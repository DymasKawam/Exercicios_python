'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

valores = (int(input('Digite 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')))

print(f'O valores digitados foram: {valores}')
print(f'O valor 9 aparece {valores.count(9)}')
if 3 in valores:
    print(f'O primeiro 3 aparece em na {valores.index(3) + 1}º')
else:
    print('Nao foi digitado nenhum 3')
print('Os pares digitados foram: ', end='')
for n in valores:
    if n % 2 ==0:
        print(f'{n} ',end='')