'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

total = 0
jogador = {}
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantas partidas {jogador['nome']} jogou: '))
    jogador['gols'] = []

    for c in range (0, jogos):
        jogador['gols'].append(int(input(f'Gols na partida {c}?: ')))
        total += jogador['gols'][c]
    jogador['total'] = total
    cont = str(input('Deseja continuar[S/N]: ')).strip()
    while cont not in 'SsNn':
        cont = str(input('Valor incorreto!! Digite somente S para sim e N para não: '))
    if cont in 'Nn':
        break
print()