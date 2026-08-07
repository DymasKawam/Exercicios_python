lista = []
opcao = 0
pp = True

while pp:
    raio = float(input('Digite o Raio: '))
    if raio <= 0:
        print('raio inválida! Digite um valor maior que 0')
        break
    altura = float(input('Digite a altura: '))
    if altura <= 0:
        print('Altura inválida! Digite um valor maior que 0')
        break
    lista.append(3.14159 * raio * raio * altura)
    conti = str(input('Deseja continuar [S/N]: ')).strip()
    if conti in 'Nn':
        break

while opcao != 6:
    print('Para ver lista [1]')
    print('Exibir apenas números pares [2]')
    print('Exibir apenas números ímpares [3]')
    print('Exibir quantidade de números pares nas posições ímpares [4]')
    print('Exibir quantidade de números impares nas posições pares [5]')
    opcao = int(input('Digite sua opcao: '))
    match opcao:
        case opcao == 1: