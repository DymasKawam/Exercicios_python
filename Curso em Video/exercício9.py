
'''
9) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa  pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.  '''
cont = 1
from datetime import datetime
dia = int(input('Dia que nasceu: '))
mes = int(input('Mes que nasceu: '))
ano = int(input('Ano que nasceu: '))
data = datetime.now()

#aqui pega a quantidade de anos que ele tem apartir do ano de nascimento
ano_con = data.year - ano

#quantos messe completos ele tem?
#
if data.month < mes:
    ano_con -= 1
    while cont < data.month:
        cont += 1
    cont += 12 - mes 
    mes_con = cont * 30
else:
    mes_con = data.month - mes
#quantos dias sobraram depois desses messes?
if data.day < dia:
    mes_con -= 1 
dia_con = data.day - dia

soma = (ano_con * 365) + mes_con + dia_con

print(ano_con * 365, mes_con, dia_con, soma)