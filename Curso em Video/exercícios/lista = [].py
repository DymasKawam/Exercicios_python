#váriaveis que eu usarei
lista = []
opcao = 0
pp = True

while pp:
    raio = float(input('Digite o Raio: '))
    if raio <= 0:
        print('raio inválida! Digite um valor maior que 0')
        continue

    altura = float(input('Digite a altura: '))
    if altura <= 0:
        print('Altura inválida! Digite um valor maior que 0')
        continue

    lista.append(3.14159 * raio * raio * altura)
    conti = str(input('Deseja continuar [S/N]: ')).strip()
    if conti in 'Nn':
        pp = False

while opcao != 6:
    print('-=' * 10)
    print('Para ver lista [1]')
    print('Exibir apenas números pares [2]')
    print('Exibir apenas números ímpares [3]')
    print('Exibir quantidade de números pares nas posições ímpares [4]')
    print('Exibir quantidade de números impares nas posições pares [5]')
    opcao = int(input('Digite sua opcao: '))

    if opcao == 1:
        print('Os números da lista são: ',end='')
        for c in lista:
            print(f' [{c:.2f}]', end='')
        print()

    elif opcao == 2:
        print('Os números pares são: ', end='')
        for c in lista:
            if c % 2 == 0:
                print(f'[{c:.2f}]', end='')

        print()

    print('-=' * 10)