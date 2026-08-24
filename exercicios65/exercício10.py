'''10) Escrever um programa que leia dois números inteiros e mostre todos os relacionamentos de ordem existentes
entre eles. Os relacionamentos possíveis são: Igual, Não igual, Maior, Menor, Maior ou igual, Menor ou igual.'''

num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))

if num1 == num2:
    print(f'[{num1}] == [{num2}]')
else: 
    print(f'[{num1}] != [{num2}]')
if num1 > num2:
    print(f'[{num1}] > [{num2}]')
if num1 < num2:
    print(f'[{num1}] < [{num2}]')
if num1 >= num2:
    print(f'[{num1}] >= [{num2}]')
else:
    print(f'[{num1}] <= [{num2}]')
