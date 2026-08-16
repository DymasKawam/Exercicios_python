'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
alunos = []
opcao = 0
while True:
    nome = str(input('nome: ')).strip().title()
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    conti = str(input('Deseja continuar[S/N]: ')).strip()
    if conti in "Nn":
        break

print('-=' * 30)
print(f'{'No.':<4}{'Nome':<10}{'média':>8}')
print('-' * 30)
for i, v in enumerate(alunos):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8}')
while True:
    print('-=' * 30)
    opcao = int(input('Escolher a nota de qual aluno[999 para parar]: '))
    if opcao == 999:
        break
    print(f'Notas de {alunos[opcao][0]}: {alunos[opcao][1]}')
