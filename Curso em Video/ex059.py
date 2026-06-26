'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
escolha = 0
valorA = int(input('Digite 1º valor: '))
valorB = int(input('Digite 2º valor: '))
while escolha != 5: 
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    escolha = int(input('Faça sua escolha: '))
    if escolha == 1:
        soma = valorA + valorB
        print('A soma entre {} e {} é igual a {}.'.format(valorA,valorB,soma))
    elif escolha == 2:
        mult = valorA * valorB
        print('A multiplicação entre {} e {} é igual a {}.'.format(valorA, valorB,mult))
    elif escolha == 3:
        if valorA > valorB:
            print('Entre {} e {} o maior valor é {}'.format(valorA, valorB, valorA))
        else:
            print('Entre {} e {} o maior valor é {}.'.format(valorB))
    elif escolha == 4:
        valorA = int(input('Digite o novo valor 1: '))
        valorB = int(input('Digite o novo valor 2: '))
    elif escolha != 5 and escolha > 5:
        print('escolha invalida tente novamente')