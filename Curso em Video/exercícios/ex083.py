'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta'''
expre = str(input('Digite sua expressão'))
lista = []
for paren in expre:
    if paren == '(':
        lista.append('(')
    elif paren == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')