"""Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. """

'''esses dois vao servir para ler o primeiro termo da PA e a razão da PA'''
primeiro = int(input('Qual é o primeiro termo da razão: '))
razão = int(input('Qual é a razão da PA: '))

'''cont vai servir para contar o total de termos que tem na PA'''
cont = 1

'''o termo vai servir para mostrar na tela os termos da PA'''
termo = primeiro

'''Mais serve para adicionar a quantidade de termos que o usuario pedir'''
mais = 1
'''O while vai contar os 10 primeiros termos'''
while cont <= 10:
    print('{} -->'.format(termo), end='')
    termo += razão
    cont += 1

'''esse while vai contar servir para quando quiserem adicionar mais termos, entretanto caso nao queiram adicionar, colocarao 0 e o while terminará'''
while mais != 0:
    mais = int(input('Digite a quantidade de termos que você quer adicionar: '))
    for c in range (0, mais):
            print('{} -->'.format(termo), end='')
            termo += razão
            cont += 1
print('A quantidade de termo foi de {}'.format(cont))