'''Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''
cid = str(input('Qual é a Cidade que você nasceu?: ')).strip().lower()
s = cid.split()
print('santo' in s[0])