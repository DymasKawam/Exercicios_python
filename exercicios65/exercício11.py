'''11) Ler dois valores inteiros para as variáveis A e B, efetuar a troca dos valores de modo que a variável A passe a
possuir o valor da variável B, e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.
'''
#pega os valores da váriavel A e B.
a = int(input('A: '))
b = int(input('B: '))

#Troca os valores das váriaveis.
a, b = b, a
print(f'A: {a}. B: {b}')