'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format('Loja DymaS'))
preco = float(input('Preço das compras: R$'))
print('''Formas de pagamento
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))


if opcao == 1:
    desconto = preco - (10/100 * preco)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, desconto))


elif opcao == 2: 
    desconto = preco - (5/100 * preco)
    print('Sua compra dee R${:.2f} vai custar R${:.2f} no final'.format(preco, desconto))


elif opcao == 3:
    nparcela = preco / 2 
    print('Sua compra sera parcelada em 2x de R${:.2f}. Sem juros'.format(nparcela))


elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = preco + (preco * 20/100)
    nparcelas = total / parcelas 
    print('Sua compra será parcelada em {:.2f}x de R${:.2f}, com juros'.format(parcelas, nparcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
else:
    print('Opção Invalida! Insira uma opção válida para continuar. ')