'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
cont = 0
alunos = []
while True:
    alunos.append(str(input('Digite o nome do aluno: ')).title().strip())
    alunos[cont].append(float(input('Digite a primeira nota: ')))
    alunos[cont].append(float(input('Digite a segunda nota: ')))

    continuar = str(input('Deseja continuar?[S/N]: ')).strip()[0]
    while continuar not in 'SsNn':
        print('Valor inválido')
        continuar = str(input('Deseja continuar?[S/N]: ')).strip()[0]
    if continuar in 'Nn':
        break
    cont += 1
print(alunos)