'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lista = []
for c in range (0,5):
    val = int(input("Digite um valor: "))
    if c == 0 or val > lista[-1]:
        lista.append(val)
    else:
        index = 0
        while index < len(lista):
            if val < lista[index]:
                lista.insert(index, val)
                break
            index += 1
print(lista)