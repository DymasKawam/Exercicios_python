"""Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. """

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1 
termo = primeiro 
mais = 10
total = 0 
while mais != 0:
    total += mais 
    while  cont <= total:
        print('{} --> '.format(termo), end='')
        termo += razao
        cont += 1
    mais = int(input('Digite quantos mais você quer colocar (0 para terminar o programa:)'))
print('A quantidade de termos foi {}'.format(total))