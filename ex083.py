'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta'''
cont1 = cont2 = ind= 0
expre = str(input('Digite sua expressão: ')).strip()
while ind < len(expre):
    if expre[ind] == '(':
        cont1 += 1
    if expre[ind] == ')':
        cont2 += 1
    ind += 1
print(cont1, cont2)
if cont1 == cont2:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é invalida!')