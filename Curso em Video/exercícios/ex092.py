'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

'''
from datetime import date
data = date.today()

print('== Registro de trabalhador ==')

trabalhador = {}
trabalhador['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = data.year - nasc
trabalhador['CTPS'] = int(input('Carteira de trabalho[0 se não tem]: '))

data = date.today()
if trabalhador['CTPS'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Digite o salário: '))
    trabalhador['aposentar'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - data.year)

print('-=' * 30)

for K, V in trabalhador.items():
    print(f'- {K} tem valor {V}')
    
