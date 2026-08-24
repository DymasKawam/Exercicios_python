raio = float(input('Digite o raio: '))
while raio<= 0:
    print('raio inválido! Digite novamente.')
    raio = float(input('Digite o raio: '))
altura = float(input('Digite a altura: '))
while altura <= 0:
    print('Altura inválida! Digite novamente')
    altura = float(input('Digite a altura: '))
resultado = 3.14159 * raio * raio * altura
print(f'O volume é {resultado:.2f}')  