'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’) 
Saída:
~~~~~~~~~
Olá Mundo!
~~~~~~~~~ '''

def escreva(txt):
    tam = len (txt)
    print('-' * (tam + 4))
    print(f'  {txt}  ')
    print('-' * (tam + 4))

text = str(input('Digite um texto: '))
escreva(text)