'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''
colocação = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Athletico-PR', 'Bahia', 'Coritiba', 'Botafogo', 'Bragantino', 'Vasco da Gama', 'Grêmio', 'Cruzeiro', 'EC Vitória', 'Corinthians', 'Atletico-MG', 'Internacional', 'Santos', 'Mirassol', 'Remo', 'Chapecoense' )

print('-=' * 30)
print(f'Os time que estão no brasileirão são: {colocação}')
print('-=' * 30)
print(f'Os cincos primeiros são: {colocação[:5]}')
print('-=' * 30)
print(f'Os ultimos quatros são {colocação[16:]}')
print('-=' * 30)
print(f'Os time em orem alfabética: {sorted(colocação)}')
print('-=' * 30)
print(f'O chapecoense está na posição: {colocação.index("Chapecoense") + 1}ª')