#faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

print('-=' * 30)
print(f'{"JOGO DE IMPAR OU PAR":^60}')
print('SE VOCE GANHAR O JOGO CONTINUA, SE PERDER ELE PARA.')
print('-=' * 30)
sequencia = 0
from random import randint
while True:
    n = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    nC = randint(0,10)
    soma = n + nC
    if soma % 2 == 0:
        if escolha == 'P':
            resultado = 'VOCÊ GANHOU'
        elif escolha == 'I':
            resultado = 'VOCÊ PERDEU'
    elif soma % 2 != 0: 
        if escolha == 'I':
            resultado = 'VOCÊ GANHOU'
        elif escolha == 'P':
            resultado = 'VOCÊ PERDEU'

    print('--' * 30)
    print(f'Seu número é {n} e você escolheu {escolha}.')
    print(f' O número do computador é {nC}.')
    print(f'--> A soma foi {soma} e o resultado foi: {resultado}')
    if resultado == 'VOCÊ PERDEU':
        break
    if resultado == 'VOCÊ GANHOU':
        print('Vamos jogar novamente...')
        print('--' * 30)
        sequencia += 1
print(f'Jogo terminado, sua sequencia de vitória foi de {sequencia}')            