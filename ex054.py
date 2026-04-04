'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

'Importando do modulo Datetime a classe date que vai mostrar o ano atual'
from datetime import date
'variavel que conta quantos adultos tem'
adulto = 0 
'Variavel que conta quantos menores de idade tem'
menor = 0   
'Criando uma estrutura de repetição que vai contar 1 ate o 7 (está em 8 porque o python sempre conta 1 a menos do que o colocado)'
for c in range (1,8):
    'a variavel ano_nascimento que esta como inteiro vai pegar os anos em que as pessoas nasceram.'
    ano_nascimento = int(input('Em que ano a {} º pessoa nasceu?: '.format(c)))
    'essa variavel vai fazer o calculo para saber a idade da pessoa'
    idade = date.today().year - ano_nascimento
    'E essa condição vai adicionar a quantidade de pessoas que sao maiores e menores'
    if idade >= 18:
        adulto += 1
    else:
        menor += 1
'e aqui vai mostrar na tela o adultos e menores no total'
print('Ao todo tivemos {} maior de idade ' \
'e {} menor de idade'.format(adulto, menor))