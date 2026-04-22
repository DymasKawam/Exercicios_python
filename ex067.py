#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número for negativo.
n = cont = 0
while True:
    n = int(input('Digite o número da tabuada [-1 ou menos para parar]: '))
    if n < 0: 
        break
    for cont in range (0,11):
        mult = n * cont
        print(f'{n} * {cont}: {mult}')
print('TABUADA ENCERRADA')