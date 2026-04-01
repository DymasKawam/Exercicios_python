"Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."
palavra = str(input('Digite uma palavra: ')).replace(' ', '').upper().strip
inverso = palavra[::-1]
print('A palavra {} estando inverso é {}'.format(palavra, inverso))
if palavra == inverso:
    print('é um palíndromo')
else:
    print('Não é um palíndromo')