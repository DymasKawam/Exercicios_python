'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

time = []
jogador = {}
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'    Quantas partidas {jogador['nome']} jogou: '))
    jogador['gols'] = []

    total = 0
    for c in range (0, jogos):
        jogador['gols'].append(int(input(f'Gols na partida {c + 1}?: ')))
        total += jogador['gols'][c]

    jogador['total'] = total
    time.append(jogador.copy())

    cont = str(input('Deseja continuar[S/N]: ')).strip()
    while cont not in 'SsNn':
        cont = str(input('Valor incorreto!! Digite somente S para sim e N para não: '))
    if cont in 'Nn':
        break

print('-=' * 30)

print(f'{'Cod':<5} {'Nome':<15} {'Gols':<15} {'total':<15}')
for i ,c in enumerate(time):
    print(f'{i:<5} ', end='')
    for d in c.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-=' * 30)
while True:
    opção = int(input('Mostrar dados de qual jogador?[999 para parar]: '))
    if opção == 999:
        break
    if opção > (len(time) - 1) or opção <= -1:
        print('Opção inválida! tente novamente')
        continue
    else:
        print('-=' * 30)
        print(f'-- APROVEITAMENTO DO JOGADOR {str(time[opção]['nome'])} --')
        for i, v in enumerate(time[opção]['gols']):
            print(f'Na partida {i + 1} fez {v} gols')
        print('-=' * 30)
print('Volte sempre!')
