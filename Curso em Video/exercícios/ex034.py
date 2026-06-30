salário = float(input('Digite seu salário: R$'))
if salário <= 1250:
    aumento = (salário * 0.15) + salário
    print('Quem ganhava R${} vai começar a receber R${}'.format(salário, aumento))
else:
    aumento = (salário * 0.10) + salário
    print('Quem ganhava R${} vai começar a receber R${}'.format(salário, aumento))