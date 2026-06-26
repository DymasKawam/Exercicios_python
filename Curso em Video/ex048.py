'''Faça um programa que calcule a soma entre todos os número ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500'''
print('A soma dos número ímpares que são múltiplos de três até 500 é igual : ')
s = 0
for c in range (1,501):
    if c % 3 == 0 and c % 2 != 0:
        s = c + s
print(s)