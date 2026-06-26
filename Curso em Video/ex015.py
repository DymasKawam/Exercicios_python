dias = int(input("Quantos dias alugado? "))
kms = float(input('Quanto Kms rodados? '))
#R$60 a diária e R$0,15 por km rodado
total = (dias * 60) + (kms * 0.15) 
print('O total a pagar é de R${:.2f}'.format(total)) 