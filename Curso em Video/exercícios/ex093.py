'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
total = 0
jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantas partidas {jogador['nome']} jogou: '))
jogador['gols'] = []

for c in range (0,jogos):
    jogador['gols'].append(int(input(f'Gols na partida {c}?: ')))
    total += jogador['gols'][c]
jogador['total'] = total

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items() :
    print(f'No campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {jogos} partidas.')
for i, v in enumerate (jogador['gols']):
    print(f'    Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')