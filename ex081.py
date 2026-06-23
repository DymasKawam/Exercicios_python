'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: 
A) Quantos números foram digitados. 
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
ind = conta = 0
while True:
    lista.append(int(input('Digite um valor inteiro: ')))
    cont = str(input('Deseja continuar: [S/N]: '))
    if cont not in 'NnSs':
        print('Digite um valor valido')
        while cont not in 'SsNn':
            cont = str(input('Deseja continuar: [S:N]: '))
    if cont in "NnSs":
        if cont in 'Nn':
            break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números nessa lista')
print(f'A lista em ordenada em forma descrecente {lista}')
print('O número 5 foi digitado ', end='')
while ind < len(lista):
    if lista[ind] == 5:
        conta += 1
    ind += 1
print(conta, ' vez')
    