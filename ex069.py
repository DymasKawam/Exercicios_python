'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos. '''

print('-=' * 30)
print(f'{"CADASTRO DE PESSOAS":^60}')
print('-=' * 30)
mais18 = homens = menos20 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            menos20 += 1
    print('-=' * 30)
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    print('-=' * 30)
    if continuar == 'N':
        break
print(f'''Nesses cadastros {mais18} pessoas tem mais de 18 anos.
      {homens} Homens foram cadastrados.
      E {menos20} mulheres tem menos de 20 anos.''')
