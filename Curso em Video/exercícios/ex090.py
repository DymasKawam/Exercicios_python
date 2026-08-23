'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

boletinho = {}
boletinho['aluno'] = str(input('Nome do aluno: '))
boletinho['média'] = int(input(f'média de {boletinho["aluno"]}:'))
if boletinho['média'] >= 7:
    boletinho['resultado'] = 'aprovado'
elif boletinho['média'] >=5:
    boletinho['resultado'] = 'recuperação'
else:
    boletinho['resultado'] = 'reprovado'

print(f'O {boletinho["aluno"]} teve a média: {boletinho["média"]}. Situação {boletinho["resultado"]}')