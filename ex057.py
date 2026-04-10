'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    entrada = str(input('Digite seu sexo [M/F]:')).upper().strip()
    if entrada == '':
        print('Você nao digitou nada')
    else:
        sexo = entrada[0]
    if sexo != 'M' and sexo != "F": 
        print('SEXO INCORRETO!!! Selecione um sexo valido! [M/F]')
    
print('O seu sexo é {}'.format(sexo))