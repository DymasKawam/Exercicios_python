
'''
9) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa  pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
'''
from datetime import date
ano_nasc = int(input('Ano de nascimento: '))
mes_nasc = int(input('Mes de nascimento: '))
dia_nasc = int(input('Dia de nascimento: '))
data = date.today()

dias_nasci = (ano_nasc * 365) + (mes_nasc * 30) + dia_nasc
dias_atual = (data.year * 365) + (data.month * 30) + data.day

resultado =  dias_atual - dias_nasci

print(resultado)