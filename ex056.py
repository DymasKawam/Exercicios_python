'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos'''
idadetot = 0
maior_idadeH = 0
totalF = 0 
homem_nome = '' 
for pess in range (1,5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    idadetot = idadetot + idade
    media = idadetot / pess
    if sexo == 'M':
        if idade > maior_idadeH:
            maior_idadeH = idade
            homem_nome = nome 
    else:
        if idade < 20:
            totalF += 1
print('A média de idade do grupo foi de {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idadeH, homem_nome))
print('Ao todo sao {} mulher(es) com menos de 20 anos'.format(totalF))