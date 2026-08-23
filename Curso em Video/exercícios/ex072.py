'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

num = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
exten = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número entre 0, 20: '))
    while n not in num:
        n = int(input('ERRO! Digite um número entre 0 e 20: '))
    print(f'O seu número escolhido foi {exten[n]}')
    con = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    while con not in 'SsNn':
        con = str(input('ERRO! Digite novamente[S/N]: ')).upper().strip()[0]
    if con == 'N':
        break